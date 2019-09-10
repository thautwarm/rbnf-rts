import operator
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.rbnf_api import codegen
from rbnf_rts.token import Token
from pathlib import Path
import ast
from subprocess import CalledProcessError

grammar_file = "./case1_grammar.rbnf"
py_file = "./case1_test.py"
tdir = "./"
tdir = Path(tdir)
with (tdir / grammar_file).open("w") as f:
    f.write("""
Mul  ::= !lhs=<Mul> ("*" | "mult") !rhs=<Atom> -> mul(lhs, rhs);
Mul  ::= !a=<Atom>                  -> a;
Atom ::= "(" !a=<Mul> ")"           -> a;
Atom ::= !a=number                  -> unwrap(a);

TOP  ::= BOF !a=<Mul> EOF           -> a;
""")
try:
    codegen((tdir / grammar_file), (tdir / py_file), k=1, inline=False, traceback=True)
except CalledProcessError as e:
    print(e.stderr)
    exit(0)
    raise Exception

with (tdir / py_file).open('r') as f:
    code = f.read()

gencode = ast.parse(code)

lexicals, run_lexer = lexer(
    r(number='\d+'), l["mult"], l["*"], l(space=" "), l['('], l[')'], ignores=['space'])


def unwrap(x: Token):
    return int(x.value)


scope = link(
    lexicals, gencode, scope=dict(unwrap=unwrap, mul=operator.mul), filename=py_file)

tokens = list(run_lexer("<current file>", "1 * 2 mult 3 mult"))
got = scope['parse_TOP'](State(), Tokens(tokens))
print(got)
