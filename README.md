# rbnf-rts
Runtime support for generated parsers of RBNF.hs

P.S: `rbnf-rts` is the new fastest Python parser generator, according to the benchmark given by,


![Bench]()


# More Examples

Check the `test` directory:

- test
    - multiply : parser/lexer implementation for multiplications
    - arith : parser/lexer implementation for arithmetics
    - relax : parser/lexer implementation for a full-featured programming language
    - llvmir: parser/lexer implementation for LLVM IR, nearly full-featured

**In each sub-directory of test, you can run tests via directly invoking the test.sh.**, like `cd test/llvmir && bash test.sh`


# Native Dependencies

- The Haskell Stack Toolchain

- The executable `rbnf-pgen` in PATH.

    If `~/.local/bin` is already in PATH:
    ```
    git clone https://github.com/thautwarm/RBNF.hs
    cd RBNF.hs
    stack install .
    ```

# Example: Multiplications

1. write a `multiply.rbnf` file:

```
# 'mul' is a python global which should be marked as 'required' in .rlex
Mul    : !lhs=Mul "*" !rhs=Atom            -> mul(lhs, rhs);
Mul    : !a=Atom                           -> a;
Atom   : "(" !a=Mul ")"                    -> a;

# 'unwrap' should be marked as 'required', just as 'mul'
Atom   : !a=<number>                       -> unwrap(a);
START ::= <BOF> !a=Mul <EOF>               -> a;
```

2. write a `multiply.rlex` file:
```
%require mul
%require unwrap
%ignore space
number [+-]?\d+
space \s+
```

3. codegen

```shell
sh> rbnf-pygen multiply.rbnf multiply.rlex multiply.py --k 1 --traceback
```

4. run statically-generated parsers and lexers and enjoy its efficiency
```python
from rbnf_rts.rts import Tokens, State
from multiply import run_lexer, mk_parser
import operator

def unwrap(x: Token):
    return int(x.value)

scope = dict(mul=operator.mul, unwrap=unwrap)

parse = mk_parser(**scope)


tokens = list(run_lexer("<current file>", "-1 * 2 * (3 * 4)"))
got = parse(State(), Tokens(tokens))
print(got)
```

Got `(True, -24)`, where `True` indicates the parsing succeeded.

If `False`, a list of errors will be given in the second element of
the return tuple.