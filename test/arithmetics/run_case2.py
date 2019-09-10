import operator
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.rbnf_api import codegen
from rbnf_rts.token import Token
from pathlib import Path
import ast
from subprocess import CalledProcessError

grammar_file = "./case2_grammar.rbnf"
py_file = "./case2_test.py"
tdir = "./"
tdir = Path(tdir)
with (tdir / grammar_file).open("w") as f:
    f.write(""" 
Mul  ::= !lhs=<Mul> !op=("*" | "/") !rhs=<Atom>  -> ArithCall(op, lhs, rhs);
Mul  ::= !a=<Atom>                               -> a;
Add  ::= !lhs=<Add> !op=("+" | "-") !rhs=<Mul>   -> ArithCall(op, lhs, rhs);
Add  ::= !a=<Mul>                                -> a;
Atom ::= "(" !a=<Add> ")"                        -> a;
Atom ::= !a=number                               -> unwrap(a);

TOP  ::= BOF !a=<Add> EOF                        -> a;
""")
try:
    codegen((tdir / grammar_file), (tdir / py_file), k=1, inline=False, traceback=True)
except CalledProcessError as e:
    print(e.stderr)
    exit(0)
    raise Exception

with (tdir / py_file).open('r') as f:
    code = f.read()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def arith_call(op: Token, lhs, rhs):
    return ops[op.value](lhs, rhs)


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


scope = link(
    lexicals, gencode, scope=dict(unwrap=unwrap, ArithCall=arith_call), filename=py_file)

tokens = list(run_lexer("<current file>", "1 * 2 + 3 * 4"))
got = scope['parse_TOP'](State(), Tokens(tokens))
print(got)

st = State()
tks = Tokens(tokens)
from timeit import timeit

import rbnf.zero as ze

f = ze.compile("""
import std.common.[Number Space]
[python] import functools.[reduce]
[python] import operator.[add sub mul truediv floordiv mod]
ignore [Space]

Numeric ::= ['-' as neg] Number as integral ['.' Number as floating]
            rewrite
                r = float(integral.value + '.' + floating.value) if floating else int(integral.value)
                -r if neg else r

Mul ::= Numeric as head (('*' | '/') as op Numeric)* as tail
        rewrite
            if tail:
                op = None
                for each in tail:
                    if op is None:
                        op = {
                            '*' : mul, '/' : floordiv
                        }[each.value]
                    else:
                        head = op(head, each)
                        op = None
            head

Atom ::= Numeric as value | '(' Add as value ')'
         rewrite value


Add ::= Mul as head (('+' | '-') as op Mul)* as tail
        rewrite
            if tail:
                op = None
                for each in tail:
                    if op is None:
                        op = {'+': add, '-': sub}[each.value]
                    else:
                        head = op(head, each)
                        op = None
            head
""")

source = """1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13"""


def rbnf_hs(text, t=10000):
    print(
        timeit(
            f"""parse_TOP(None, Tokens(list(run_lexer("current_file", {repr(text)}))))""",
            globals=dict(
                parse_TOP=scope['parse_TOP'],
                Tokens=Tokens,
                run_lexer=run_lexer,
            ),
            number=t))


def rbnf_py(text, t=10000):
    print(timeit(f"""match(f{text})""", globals=dict(match=f.match), number=t))


print(f.match(source).result)

tokens = list(run_lexer("<current file>", source))
got = scope['parse_TOP'](State(), Tokens(tokens))
print(got)

t = 20000
rbnf_hs(source, t)
rbnf_hs(source, t)

