from rbnf_rts.parser_gen import *
from rbnf_rts.rts import Tokens, State, AST
from rbnf_rts import bootstrap

__all__ = ['parse']


def parse(text: str, filename: str = "unknown"):
    p = bootstrap.Parser()

    _parse = mk_parser(empty=bootstrap.empty,
                       cons=bootstrap.cons,
                       singleton=bootstrap.singleton,
                       literal=p.literal,
                       terminal=p.terminal,
                       nonterm=p.nonterm,
                       optional=p.optional,
                       nonseplist=p.list,
                       seplist=p.seplist,
                       alias=p.alias,
                       seq=p.seq,
                       action=p.action,
                       prod=p.prod,
                       symbol=p.symbol,
                       integer=p.integer,
                       call=p.call,
                       mktuple=p.mktuple,
                       alt=p.alt,
                       newscope=p.newscope,
                       ith=p.ith,
                       spelling=p.spelling,
                       mklist=p.mklist,
                       tupletail=p.tupletail,
                       location=p.location)
    tokens = list(run_lexer(filename, text))
    res = _parse(State(), Tokens(tokens))
    if res[0]:
        from io import StringIO
        with StringIO() as o:
            for prod in p.prods:
                o.write(prod)
                o.write(';\n')
            return o.getvalue()
    msgs = []
    for each in res[1]:
        i, msg = each
        token = tokens[i]
        lineno = token.lineno
        colno = token.colno
        msgs.append(f"Line {lineno}, column {colno}, {msg}")
    raise SyntaxError(f"Filename {filename}:\n" + "\n".join(msgs))


