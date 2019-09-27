from prettyprinter import register_pretty, pretty_call, pprint
from .rts import Tokens, AST


@register_pretty(Tokens)
def pretty_tokens(value, ctx):
    return pretty_call(
        ctx, Tokens, offset=value.offset, array=value.array)


@register_pretty(AST)
def pretty_tokens(value, ctx):
    return pretty_call(ctx, AST, tag=value.tag, contents=value.contents)
