import ast
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.utils import ImmutableMap
from rbnf_rts.lexical import *
from pathlib import Path

py_file = "./grammar.py"

rev_map = {}

with Path("grammar.rbnf-lex").open() as f:
    for line in f.read().splitlines():
        if line.startswith('quote '):
            rev_map[line[6:]] = line

with Path(py_file).open() as f:
    code = f.read()

gencode = ast.parse(code)

lexicals, run_lexer = lexer(
    r(number="[-+]?[0-9]+(\.[eE][-+]?\d+)?"),
    r(space="\s"),
    r(identifier="[a-zA-Z_]{1}[a-zA-Z_0-9]*"),
    r(str=r'"([^\\"]+|\\.)*?"'),
    l['->'],
    l[','],
    l['{'],
    l['}'],
    l['('],
    l[')'],
    l['.'],
    l['='],
    l['|'],
    l['^'],
    ignores=['space'],
    reserved_map=ImmutableMap.from_dict(rev_map))

scope = link(lexicals, gencode, scope=None, filename=py_file)

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
for e in tokens:
    print(e)
got = scope['parse_START'](State(), Tokens(tokens))
print(got)
