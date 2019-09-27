from rbnf_rts.rts import Tokens, State
from relax import run_lexer, mk_parser
parse = mk_parser()

tokens = list(
    run_lexer(
        "<current file>", """
module F = {
    let x = 1
    let main = fun a b c ->
        match a(b, c) with
        | ^a -> 2
}
"""))
print(parse(State(), Tokens(tokens)))
