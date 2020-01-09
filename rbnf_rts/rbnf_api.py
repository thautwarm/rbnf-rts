import sys
import re
from subprocess import check_call
from wisepy2 import wise
from pathlib import Path
from .generator import Generator
from .plot import view_parsing_graph
from .unparse import Unparser
from io import StringIO


def codegen(filename: str,
            out: str,
            inline=True,
            k: int = 1,
            traceback: bool = True):
    """
filename: grammar filename

inline: flag to indicate if use grammar inline optimisation.

k: maximum Lookahead count.

out: storing generated python code

traceback: whether to support good error messaging in generated code. With overhead.
    """

    assert k > 0
    cmd = [
        "rbnf-pgen", "-in", filename, "-k",
        str(k), "-out", out, "-be", "python"
    ]
    if traceback:
        cmd.append("--trace")
    if not inline:
        cmd.append("--noinline")
    check_call(cmd)


def dump_graph(filename: str, out: str, *, inline: bool = False):
    """
    :param filename: grammar filename
    :param inline: flag to indicate if use grammar inline optimisation.
    :param out: JSON filename
    """
    cmd = [
        "rbnf-pgen", "-in", filename, "-jsongraph", out, "-be", "python"
    ]
    if not inline:
        print('noinline')
        cmd.append("--noinline")
    check_call(cmd)


def cli_dump_graph():
    wise(dump_graph)(sys.argv[1:])


def cli_view_graph():
    wise(view_parsing_graph)(sys.argv[1:])


comment = re.compile(r"#[^\n\r]*")


def generate(bnf_filename: str,
             lex_filename: str,
             out: str,
             *,
             k: int = 1, inline=False,
             traceback: bool = False,
             stoppable_lr: bool = False):
    """
bnf_filename: .rbnf filename
lex_filename: .rlex filename
out: .py filename
inline: flag to indicate if use grammar inline optimisation.
k: maximum Lookahead count.
out: storing generated python code
traceback: whether to support good error messaging in generated code. With overhead.
stoppable_lr: allow rollbacks during proceeding the left recursion branch
    """
    out_file = Path(out)
    to_remove = []

    lex_terms_file = out_file.with_suffix(".rlex-terms-tmp")
    to_remove.append(lex_terms_file)

    py_parser_tmp_file = out_file.with_suffix(".py-tmp")
    to_remove.append(py_parser_tmp_file)

    if bnf_filename.endswith('.exrbnf'):
        from rbnf_rts.exrbnf_parser import parse
        with open(bnf_filename) as f:
            source = f.read()
            source = comment.sub('', source)
            haskell_rbnf_source = parse(source, bnf_filename)

        rbnf_plus_file = out_file.with_suffix(".extended.rbnf")
        to_remove.append(rbnf_plus_file)
        with open(rbnf_plus_file, 'w') as f:
            f.write(haskell_rbnf_source)
        bnf_filename = str(rbnf_plus_file)

    assert k > 0
    cmd = [
        "rbnf-pgen", "-in", bnf_filename, "-k",
        str(k), "-out",
        str(py_parser_tmp_file), "-be", "python"
    ]
    if traceback:
        print('Using tracebacks')
        cmd.append("--trace")
    if not inline:
        print('Using noinline mode')
        cmd.append("--noinline")
    if stoppable_lr:
        print('Using stoppable lr(maybe bad error report for left recursions)')
        cmd.append('--stoppablelr')

    check_call(cmd)

    cmd = ['rbnf-lex', '-in', bnf_filename, '-out', str(lex_terms_file)]
    check_call(cmd)
    gen = Generator()
    lexer_ast, parser_ast = gen.gen_from_file(lex_filename,
                                              str(lex_terms_file),
                                              str(py_parser_tmp_file))
    sio = StringIO()
    sio.write(
        '# this file is auto-generated by RBNF.hs and the Python package rbnf-rts\n'
    )
    Unparser(lexer_ast, sio)
    sio.write('\n')
    Unparser(parser_ast, sio)
    with out_file.open('w') as f:
        f.write(sio.getvalue())

    for each in to_remove:
        each.unlink()


def cli_generate():
    wise(generate)(sys.argv[1:])
