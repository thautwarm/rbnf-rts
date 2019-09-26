rbnf-pgen -in ./grammar.rbnf -k 1 -out ./grammar.py -be python --noinline --trace
rbnf-lex -in grammar.rbnf -out grammar.rbnf-lex
