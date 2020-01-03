from rbnfjson.parser_generated import *
from rbnf_rts.rts import Tokens, State, AST
from rbnf_rts import routine

__all__ = ['parse']

co = mk_parser.__code__
_parse = mk_parser(**{name: getattr(routine, name) for name in co.co_varnames[:co.co_argcount]})


def parse(text: str, filename: str = "unknown") -> AST:
    tokens = list(run_lexer(filename, text))
    res = _parse(State(), Tokens(tokens))
    if res[0]:
        return res[1]

    msgs = []
    for each in res[1]:
        i, msg = each
        token = tokens[i]
        lineno = token.lineno
        colno = token.colno
        msgs.append(f"Line {lineno}, column {colno}, {msg}")
    raise SyntaxError(f"Filename {filename}:\n" + "\n".join(msgs))
