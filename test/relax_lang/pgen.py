from rbnf_rts.rts import Tokens, State
from linked_parser import run_lexer, mk_parser
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
# for e in tokens:
#     print(e)
# got = scope['parse_START'](State(), Tokens(tokens))
print(parse(State(), Tokens(tokens)))
