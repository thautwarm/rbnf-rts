from location_parser import mk_parser, lexicals, run_lexer
from rbnf_rts.rts import Tokens, State, AST

parse = mk_parser()
tokens = list(run_lexer("a.txt", "a"))
res = parse(State(), Tokens(tokens))
assert res == (True, (0, 0, 'a.txt'))
