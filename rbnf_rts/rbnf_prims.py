from prettyprinter import pformat
from typing import Generic, TypeVar, Dict, Optional
import operator
import ast

T = TypeVar('T')


class Tokens:
    __slots__ = ['array', 'offset']

    def __init__(self, array):
        self.array = array
        self.offset = 0

    def __repr__(self):
        return pformat(self)


class State:
    def __init__(self):
        pass


class AST(Generic[T]):
    __slots__ = ['tag', "contents"]

    def __init__(self, tag: str, contents: T):
        self.tag = tag
        self.contents = contents

    def __repr__(self):
        return pformat(self)


class Nil:
    nil = None
    __slots__ = []

    def __init__(self):
        if Nil.nil is None:
            Nil.nil = self
            return
        raise ValueError("Nil cannot get instantiated twice.")

    def __len__(self):
        return 0

    def __getitem__(self, n):
        raise IndexError('Out of bounds')

    @property
    def head(self):
        raise IndexError('Out of bounds')

    @property
    def tail(self):
        raise IndexError('Out of bounds')

    def __repr__(self):
        return "[]"


nil = Nil()


class Cons:
    __slots__ = ['head', 'tail']

    def __init__(self, _head, _tail):
        self.head = _head
        self.tail = _tail

    def __len__(self):
        _nil = nil
        l = 0
        while self is not _nil:
            l += 1
            # noinspection PyMethodFirstArgAssignment
            self = self.tail
        return l

    def __iter__(self):
        _nil = nil
        while self is not _nil:
            yield self.head
            # noinspection PyMethodFirstArgAssignment
            self = self.tail

    def __getitem__(self, n):
        while n != 0:
            # noinspection PyMethodFirstArgAssignment
            self = self.tail
        return self.head

    def __repr__(self):
        return repr(list(self))


def link(lexicals: Dict[str, int], gencode: ast.Module, scope: Optional[Dict], filename: str = "unknown"):
    prim__eq = operator.eq  # should specialize
    prim__not__eq = operator.ne  # should specialize
    prim__null = None  # should specialize

    # should inline
    def prim__peekable(tokens, i):
        return len(tokens.array) > tokens.offset + i

    # should inline
    def prim__peek(tokens, i):
        return tokens.array[tokens.offset + i]

    # should inline
    def prim__match__tk(tokens, idint):
        # print(tokens.offset)
        try:
            tk = tokens.array[tokens.offset]
        except IndexError:
            return None
        if tk.idint is not idint:
            return None
        tokens.offset += 1
        return tk

    # should specialize
    def prim__tk__id(s):
        return lexicals[s]

    # should inline
    def prim__reset(tokens, i):
        tokens.offset = i

    prim__cons = Cons
    prim__nil = nil

    # should eliminate
    def prim__to__result(x): return x

    # should eliminate
    def prim__to__any(x): return x

    # should inline
    def prim__mk__ast(s: str, x: T) -> AST[T]: return AST(s, x)

    # should inline
    def prim__is__null(x): return x is None

    # should inline
    def prim__is__not__null(x): return x is not None

    scope = scope or {}
    scope.update(locals())
    exec(compile(gencode, filename, "exec"), scope)
    return scope
