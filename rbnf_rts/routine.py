from rbnf_rts.rts import AST, Cons, _nil
from rbnf_rts.token import Token
from json.decoder import py_scanstring


def LRList(x: AST):
    """
    for nodes produced by
        A = [A] B
    , convert them to a sequence [B, B, ...]
    """
    res = []
    _len = len
    cs = x.contents
    while True:
        end = cs[-1]
        res.append(end)
        if _len(cs) is 1:
            break
        cs = cs[0].contents
    res.reverse()
    return res


def LRCommaList(x: AST):
    """
    for nodes produced by
        A = [A Comma] B
    , convert them to a sequence [B, B, ...]
    """
    res = []
    _len = len
    cs = x.contents
    while True:
        end = cs[-1]
        res.append(end)
        if _len(cs) is 1:
            break
        cs = cs[0][0].contents
    res.reverse()
    return res


def LRCommaSurroundedList(x: AST):
    """
    for nodes produced by
        List = _ [Elts] _
        Elts = [A Comma] B
    , convert a `List` to a sequence [B, B, ...]
    """
    x = x.contents
    if len(x) is 2:
        return []
    return LRCommaList(x[1])


def DQString(x: Token, f=py_scanstring):
    """from the raw form of a double quoted string to a python string,
    e.g.,
        dqstring('"asd"') == "asd"
    """
    return f(x.value, 1)[0]
