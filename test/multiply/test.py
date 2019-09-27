from rbnf_rts.rts import Tokens, State
from rbnf_rts.token import Token
from multiply import run_lexer, mk_parser
import operator


def unwrap(x: Token):
    return int(x.value)


scope = dict(mul=operator.mul, unwrap=unwrap)

parse = mk_parser(**scope)

tokens = list(run_lexer("<current file>", "-1 * 2 * (3 * 4)"))
got = parse(State(), Tokens(tokens))
assert got == (True, -24)
