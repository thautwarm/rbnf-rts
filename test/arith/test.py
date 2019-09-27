from rbnf_rts.rts import Tokens, State
from rbnf_rts.token import Token
from arith import run_lexer, mk_parser
import operator


def unwrap(x: Token):
    return int(x.value)


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def arith_call(op: Token, lhs, rhs):
    return ops[op.value](lhs, rhs)


scope = dict(arith=arith_call, unwrap=unwrap)

parse = mk_parser(**scope)

tokens = list(run_lexer("<current file>", "1 * -2 + 3 * 4"))
got = parse(State(), Tokens(tokens))
assert got == (True, 10)
