from rbnf_rts.exrbnf_parser import parse
import re
test = re.compile('\blist\b')
res = parse("""
a : <BOE> list('a') <EOF>;
""")
assert not test.findall(res)