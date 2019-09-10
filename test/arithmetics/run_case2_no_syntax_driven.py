from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.rbnf_api import codegen
from rbnf_rts.token import Token
from pathlib import Path
import ast
from subprocess import CalledProcessError

grammar_file = "./case2nsd_grammar.rbnf"
py_file = "./case2nsd_test.py"
tdir = "./"
tdir = Path(tdir)
with (tdir / grammar_file).open("w") as f:
    f.write(""" 
Mul  ::= <Mul> ("*" | "/") <Atom>;
Mul  ::= <Atom>                  ;
Add  ::= <Add> ("+" | "-") <Mul> ;
Add  ::= <Mul>                   ;
Atom ::= "(" <Add> ")"           ;                        
Atom ::= number                  ;                               

TOP  ::= BOF <Add> EOF           ;       
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
    r(number='\d+'),
    l["+"],
    l["-"],
    l["*"],
    l["/"],
    l(space=" "),
    l(space="\n"),
    l['('],
    l[')'],
    ignores=['space'])


def unwrap(x: Token):
    return int(x.value)


scope = link(lexicals, gencode, scope=dict(), filename=py_file)

tokens = list(run_lexer("<current file>", "1 * 2 + 3 * 4"))
_, ast = scope['parse_TOP'](State(), Tokens(tokens))
print(ast)
