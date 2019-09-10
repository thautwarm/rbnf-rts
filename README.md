# rbnf-rts
Runtime support for generated parsers of RBNF.hs


# Native Dependencies

- The Haskell Stack Toolchain

- The executable `rbnf-pgen` in PATH.

    If `~/.local/bin` is already in PATH:
    ```
    git clone https://github.com/thautwarm/RBNF.hs
    cd RBNF.hs
    stack install .
    ```

# Usage

Check test directory:

```python
import operator
from rbnf_rts.rbnf_prims import link, Tokens, State
from rbnf_rts.lexical import *
from rbnf_rts.token import Token
import ast
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
    check_output(["rbnf-pgen", "-in", filename, "-k", "1", "-out", "./case1_noinline.py", "-be", "python", "--trace",
                  "--noinline"])
    code: bytes = check_output(["rbnf-pgen", "-in", filename, "-k", "1", "-out", "stdout", "-be", "python", "--trace"])
except CalledProcessError as e:
    print(e.stderr)
    exit(0)

code = code.decode()
gencode = ast.parse(code)

lexicals, run_lexer = lexer(
    r(number='\d+'),
    l["*"],
    l(space=" "),
    l['('],
    l[')'],
    ignores=['space']
)

def unwrap(x: Token):
    return int(x.value)


scope = link(lexicals, gencode, scope=dict(unwrap=unwrap, mul=operator.mul), filename=filename)
tokens = list(run_lexer(filename, "1 * 2 * (3 * 4)"))
got = scope['parse_Mul'](State(), Tokens(tokens))
print(got)

```

Got `(True, 24)`, where `True` indicates the parsing succeeded.