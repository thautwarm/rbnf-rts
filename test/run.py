import operator
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.token import Token
import ast
import re
from subprocess import check_output, CalledProcessError

filename = "./grammar.rbnf"
with open(filename, "w") as f:
    f.write("""
Mul  ::= !lhs=<Mul> "*" !rhs=<Atom> -> mul(lhs, rhs);
Mul  ::= !a=<Atom>                  -> a;
Atom ::= "(" !a=<Mul> ")"           -> a;
Atom ::= !a=number                  -> unwrap(a);
""")

try:
    check_output(["rbnf-pgen", "-in", filename, "-k", "1", "-out", "./case1_inline.py", "-be", "python", "--trace"])
    check_output(["rbnf-pgen", "-in", filename, "-k", "1", "-out", "./case1_noinline.py", "-be", "python", "--trace", "--noinline"])
    code: bytes = check_output(["rbnf-pgen", "-in", filename, "-k", "1", "-out", "stdout", "-be", "python", "--trace"])
except CalledProcessError as e:
    print(e.stderr)
    exit(0)
    raise Exception

code = code.decode()
gencode = ast.parse(code)

number = RegexLexerDescriptor(0, re.compile("\d+"))
mult = LiteralLexerDescriptor(1, "*")
space = LiteralLexerDescriptor(2, " ")
lp = LiteralLexerDescriptor(3, "(")
rp = LiteralLexerDescriptor(4, ")")

lexicals = {"number": number.typeid, "quote *": mult.typeid, "quote (": lp.typeid, "quote )": rp.typeid}


def unwrap(x: Token):
    return int(x.value)


scope = link(lexicals, gencode, scope=dict(unwrap=unwrap, mul=operator.mul), filename=filename)
lexer_table = [mult.to_lexer(), number.to_lexer(), space.to_lexer(), lp.to_lexer(), rp.to_lexer()]
tokens = lexing(filename, "1 * 2 * (3 * 4)", lexer_table, {})
spaceid = space.typeid
tokens = [each for each in tokens if each.idint is not spaceid]
got = scope['parse_Mul'](State(), Tokens(tokens))
print(got)
