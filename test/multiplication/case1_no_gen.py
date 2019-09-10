import operator
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.rbnf_api import codegen
from rbnf_rts.token import Token
from pathlib import Path
import ast

tdir = Path('.')
py_file = "case1_test.py"
with (tdir / py_file).open('r') as f:
    code = f.read()

gencode = ast.parse(code)

lexicals, run_lexer = lexer(
    r(number='\d+'), l["*"], l(space=" "), l['('], l[')'], ignores=['space'])


def unwrap(x: Token):
    return int(x.value)


scope = link(
    lexicals, gencode, scope=dict(unwrap=unwrap, mul=operator.mul), filename=py_file)

tokens = list(run_lexer("<current file>", "1 * 2 * 3"))
got = scope['parse_TOP'](State(), Tokens(tokens))
print(got)
