import operator
from rbnf_rts.rts import Tokens, State
from rbnf_rts.rbnf_linker import link
from rbnf_rts.lexical import *
from rbnf_rts.rbnf_api import codegen
from rbnf_rts.token import Token
from rbnf_rts.unparse import Unparser
from pathlib import Path
import ast
from subprocess import CalledProcessError

grammar_file = "./case1_grammar.rbnf"
py_file = "./case1_test.py"
tdir = "./"
tdir = Path(tdir)
with (tdir / grammar_file).open("w") as f:
    f.write("""
Mul  ::= !lhs=Mul ("*" | "mult") !rhs=Atom -> mul(lhs, rhs);
Mul  ::= !a=Atom                  -> a;
Atom ::= "(" !a=Mul ")"           -> a;
Atom ::= !a=<number>                  -> unwrap(a);

START ::= <BOF> !a=Mul <EOF>           -> a;
""")
try:
    codegen((tdir / grammar_file), (tdir / py_file),
            k=1,
            inline=False,
            traceback=True)
except CalledProcessError as e:
    print(e.stderr)
    exit(0)
    raise Exception

with (tdir / py_file).open('r') as f:
    code = f.read()

gencode = ast.parse(code)

lexicals, run_lexer = lexer(
    r(number='\d+'),
    l["mult"],
    l["*"],
    l(space=" "),
    l['('],
    l[')'],
    ignores=['space'])


def unwrap(x: Token):
    return int(x.value)


scope = dict(unwrap=unwrap, mul=operator.mul)
fn = link(lexicals, gencode, requires=scope.keys())

with open("run_case1_final_parser.py", 'w') as f:
    Unparser(fn, f)

from run_case1_final_parser import mk_parser
parse = mk_parser(**scope)

tokens = list(run_lexer("<current file>", "1 * 2 mult 3"))
got = parse(State(), Tokens(tokens))
print(got)

tokens = list(run_lexer("<current file>", "1 * 2 mult 3 mult"))
got = parse(State(), Tokens(tokens))
print(got)
