from rbnf_rts.rbnf_linker import link
from textwrap import indent
from wisepy2 import wise
import re
import ast


class Generator:

    def __init__(self):
        self._regexps = []
        self._lits = []
        self._ignores = []
        self._reserved_map = {}
        self._requires = []

    def require_global(self, n: str):
        self._requires.append(n)

    def ignore(self, s: str):
        self._ignores.append(s)

    def _reserved_from_source(self, source: str):
        rev_map = self._reserved_map
        prefix = "quote "
        n = len(prefix)
        for line in source.splitlines():
            if line.startswith(prefix):
                rev_map[line[n:]] = line

    def _regex_from_source(self, src: str):
        detect_blank = re.compile("\S+")
        args = self._regexps
        for line in src.splitlines():
            line = line.strip()
            d = detect_blank.match(line)
            if not d:
                continue
            p = d.span()[1]
            name = line[:p]
            regex = line[p + 1:].strip()
            if name == "%ignore":
                name = regex
                self.ignore(name)
                continue
            elif name == "%require":
                name = regex
                self.require_global(name)
                continue

            args.append((name, regex, re.compile(regex)))

    def gen_from_file(self, lexer_f, lexer_term_f, parser_f):
        with open(lexer_f) as lexer_f, open(
                lexer_term_f) as lexer_term_f, open(
                    parser_f) as parser_f:
            return self.gen(lexer_f.read(), lexer_term_f.read(),
                            parser_f.read())

    def gen(self, lexer_src, lexer_term_src, parser_src):
        self._regex_from_source(lexer_src)
        self._reserved_from_source(lexer_term_src)
        numbering = {'BOF': 0, 'EOF': 1}

        lits = []
        for literal, quote in self._reserved_map.items():
            numbering[quote] = len(numbering)
            for _, _, regex in self._regexps:
                if regex.match(literal):
                    break
            else:
                # literal cannot be tokenized by current regex rules.
                lits.append((literal, quote))
        args = []
        for name, rule, _ in self._regexps:
            args.append(f'r({name}={rule!r})')
            numbering[name] = len(numbering)
        for lit, quote in lits:
            args.append(f'l[{lit!r}]')
        if self._ignores:
            args.append(f'ignores={self._ignores}')
        if self._reserved_map:
            args.append(
                f'reserved_map=ImmutableMap.from_dict({self._reserved_map})'
            )
        args.append(f'numbering={numbering},')
        arg_str = indent(',\n'.join(args), prefix="    ")

        lexer_code = f"""
from rbnf_rts.rbnf_linker import link
from rbnf_rts.utils import ImmutableMap
from rbnf_rts.lexical import *
_, run_lexer = lexer(
{arg_str}
)
"""
        lexer_ast = ast.parse(lexer_code)
        genast = ast.parse(parser_src)
        parser_ast = link(numbering, genast, self._requires)
        return lexer_ast, parser_ast
