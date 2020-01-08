from rbnf_rts.routine import DQString
from rbnf_rts.rts import _nil, Cons
from rbnf_rts.token import Token
import typing

empty = _nil
cons = Cons


class Numberer(dict):
    def __missing__(self, key):
        n = self[key] = len(self)
        return n


def singleton(x):
    return cons(x, empty)


class Parser:
    def __init__(self):
        self.generative_nonterm = {}
        self.prods = []
        self.locals: typing.Optional[Numberer] = Numberer()

    @classmethod
    def literal(cls, x: Token):
        return x.value

    @classmethod
    def terminal(cls, x: Token):
        return x.value

    @classmethod
    def nonterm(cls, x: Token):
        return x.value

    @classmethod
    def optional(cls, x):
        return '[ ' + x + ' ]'

    def list(self, x):
        x = '({})'.format(x)
        key = ('list', x)
        n = self.generative_nonterm.get(key, None)
        if n is None:
            n = len(self.generative_nonterm)
            n = 'rbnf_list_{}'.format(n)
            self.generative_nonterm[key] = n
            self.prods.append('{} : {} -> {}'.format(n, x, 'RBNFlist(RBNFelt(RBNFint0))'))
            self.prods.append('{} : {} {} -> {}'.format(n, n, x, "RBNFappend(RBNFelt(RBNFint0), RBNFelt(RBNFint1))"))

        return n

    def seplist(self, a, b):
        b = '({})'.format(b)
        key = ('separated_list', a, b)
        n = self.generative_nonterm.get(key, None)
        if n is None:
            n = len(self.generative_nonterm)
            n = 'rbnf_sep_list_{}'.format(n)
            self.generative_nonterm[key] = n
            self.prods.append('{} : {} -> {}'.format(n, b, 'RBNFlist(RBNFelt(RBNFint0))'))
            self.prods.append(
                    '{} : {} {} {} -> {}'.format(n, n, a, b, "RBNFappend(RBNFelt(RBNFint0), RBNFelt(RBNFint2))"))
        return n

    def alias(self, n: Token, s):
        print('aaa')
        return '!auto{}={}'.format(self.locals[n.value], s)

    def seq(self, xs):
        return ' '.join(xs)

    def action(self, rule, act):
        return rule, act

    def prod(self, n: Token, elts):
        n = n.value
        for each in elts:
            if isinstance(each, tuple):
                a, b = each
                self.prods.append('{} : {} -> {}'.format(n, a, b))
            else:
                self.prods.append('{} : {}'.format(n, each))

    @classmethod
    def mktuple(self, x=()):
        return 'RBNFtuple({})'.format(', '.join(x))

    def tupletail(self, tl):
        if tl is None:
            return lambda x: x
        return lambda hd: Parser.mktuple(cons(hd, tl))

    def mklist(self, x=()):
        return 'RBNFlist({})'.format(', '.join(x))

    def symbol(self, x: Token):
        n = x.value
        n = self.locals.get(n, n)
        if isinstance(n, int):
            n = 'auto{}'.format(n)
        return n

    def integer(self, x: Token):
        return 'RBNFint{}'.format(x.value)

    def call(self, f, args):
        return '{}({})'.format(f, ', '.join(args))

    def alt(self, xs):
        return ' | '.join(xs)

    def newscope(self, x):
        self.locals = Numberer()
        return x

    def ith(self, i):
        return 'RBNFelt({})'.format(i)

    def spelling(self, s):
        return 'RBNFvalueof({})'.format(s)
