from rbnf_rts.rts import Tokens, State
from type_sig import run_lexer, mk_parser, lexicals
parse = mk_parser()

tokens = list(
    run_lexer(
        "<current file>", """
* ** * ** *
        """))

print(lexicals)
for e in tokens:
    print(e)
print(parse(State(), Tokens(tokens)))