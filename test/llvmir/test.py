from rbnf_rts.rts import Tokens, State
from llvmir import run_lexer, mk_parser

parse = mk_parser()

sources = [
    "@gg = constant void bitcast (i8* 3 to i16*)",
    "%a = type {i8*, i1}", """
define i8 @f (void){
    %i = getelementptr i32*, i32* %j, i32 1
    ret void
}

define i32* @f(void (void*)* %g){
    %a = alloca i8, align 4
    %b = bitcast i8* %a to void*
    ret i32* %add

}
"""
]
for src in sources:
    tokens = list(run_lexer("<unknown filename>", src))
    print(parse(State(), Tokens(tokens)))
