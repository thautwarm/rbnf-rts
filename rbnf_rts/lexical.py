from .utils import ImmutableMap, Numbering, Builder
from .token import Token
from warnings import warn
import re
import abc
import typing as t

__all__ = ['lexer', 'r', 'l']
Lexer = t.Callable[[str, int], t.Optional[t.Tuple[int, str]]]


class LexerDescriptor(abc.ABC):
    typeid: int

    @abc.abstractmethod
    def to_lexer(self) -> Lexer:
        return self.to_lexer()


class RegexLexerDescriptor(LexerDescriptor):

    def __init__(self, typeid: int, regex_pat: t.Pattern):
        self.typeid = typeid
        self.regex_pat = regex_pat

    def to_lexer(self):
        match = self.regex_pat.match
        typeid = self.typeid

        def lex(string, pos):
            m = match(string, pos)
            if m:
                return m.group()

        return typeid, lex


class LiteralLexerDescriptor(LexerDescriptor):

    def __init__(self, typeid: int, *string_pats: str):
        assert string_pats
        self.typeid = typeid
        self.contents = string_pats

    def to_lexer(self):
        pats = self.contents
        typeid = self.typeid
        if len(pats) is 1:
            pats = pats[0]

            def lex(string: str, pos):
                if string.startswith(pats, pos):
                    return pats
        else:

            def lex(string: str, pos):
                for pat in pats:
                    if string.startswith(pat, pos):
                        return pat

        return typeid, lex


def lexer_reduce(lexer_descriptors: t.List[LexerDescriptor]
                 ) -> t.List[LexerDescriptor]:

    def _chunk(stream: t.Iterable[LexerDescriptor]):
        grouped = []
        _append = grouped.append
        last = None
        for _e in stream:
            e = type(_e), _e.typeid
            if last is None:
                grouped = [_e]
                _append = grouped.append
            elif last == e:
                _append(_e)
            else:
                yield (last, grouped)
                grouped = [_e]
                _append = grouped.append
            last = e
        else:
            if last:
                yield (last, grouped)

    groups = list(_chunk(lexer_descriptors))

    ret = []
    for (lexer_type, typeid), descriptors in groups:
        if lexer_type is RegexLexerDescriptor:
            ret.extend(descriptors)
        else:
            assert lexer_type is LiteralLexerDescriptor
            descriptors: t.List[LiteralLexerDescriptor]
            contents = sum(
                tuple(each.contents for each in descriptors), ())

            ret.append(LiteralLexerDescriptor(typeid, *contents))

    return ret


def lexing(filename: str, text: str, lexer_table: list,
           reserved_map: dict):
    text_length = len(text)
    colno = 0
    lineno = 0
    pos = 0
    newline = '\n'

    while True:
        if text_length <= pos:
            break

        for typeid, case in lexer_table:
            origin_word = case(text, pos)

            if origin_word is None:
                continue
            pat = origin_word
            casted_typeid = reserved_map.get(pat)
            if casted_typeid is None:
                yield Token(pos, lineno, colno, filename, typeid,
                            origin_word)
            else:
                yield Token(pos, lineno, colno, filename, casted_typeid,
                            origin_word)
            n = len(pat)
            line_inc = pat.count(newline)
            if line_inc:
                latest_newline_idx = pat.rindex(newline)
                colno = n - latest_newline_idx
                lineno += line_inc
            else:
                colno += n
            pos += n
            break

        else:
            warn(f"No handler for character `{text[pos].__repr__()}`.")
            ch = text[pos]
            origin_word = ch
            yield Token(pos, lineno, colno, filename, -1, origin_word)
            if ch == "\n":
                lineno += 1
                colno = 0
            pos += 1


def lexing_no_reverse(filename: str, text: str, lexer_table: list):
    text_length = len(text)
    colno = 0
    lineno = 0
    pos = 0
    newline = '\n'

    while True:
        if text_length <= pos:
            break

        for typeid, case in lexer_table:
            origin_word = case(text, pos)

            if origin_word is None:
                continue
            pat = origin_word
            yield Token(pos, lineno, colno, filename, typeid,
                        origin_word)

            n = len(pat)
            line_inc = pat.count(newline)
            if line_inc:
                latest_newline_idx = pat.rindex(newline)
                colno = n - latest_newline_idx
                lineno += line_inc
            else:
                colno += n
            pos += n
            break

        else:
            warn(f"No handler for character `{text[pos].__repr__()}`.")
            ch = text[pos]
            origin_word = ch
            yield Token(pos, lineno, colno, filename, -1, origin_word)
            if ch == "\n":
                lineno += 1
                colno = 0
            pos += 1


def regex_call_build(**kwargs):
    assert len(kwargs) is 1
    [(a, b)] = kwargs.items()
    return a, re.compile(b)


def regex_getitem_build(arg):
    assert isinstance(arg, str)
    return "quote " + arg, re.compile(arg)


def str_call_build(**kwargs):
    assert len(kwargs) is 1
    [(a, b)] = kwargs.items()
    return a, b


def str_getitem_build(arg):
    assert isinstance(arg, str)
    return "quote " + arg, arg


r: Builder[str, t.Tuple[str, re.Pattern]] = Builder(
    call=regex_call_build, getitem=regex_getitem_build)
l: Builder[str, t.Tuple[str, str]] = Builder(
    call=str_call_build, getitem=str_getitem_build)


def lexer(*subrules: t.Tuple[str, t.Union[re.Pattern, str]],
          ignores=(),
          reserved_map: ImmutableMap[str, str] = ImmutableMap(()),
          numbering=None):
    numbering = numbering or Numbering()
    BOF = numbering["BOF"]
    EOF = numbering["EOF"]
    sublexers = []

    for name, each in subrules:
        number = numbering[name]
        if isinstance(each, str):
            sublexers.append(LiteralLexerDescriptor(number, each))
        elif isinstance(each, re.Pattern):
            sublexers.append(RegexLexerDescriptor(number, each))
        else:
            raise TypeError(type(each))

    table = [e.to_lexer() for e in sublexers]

    reserved_map = {k: numbering[v] for k, v in reserved_map.to_list()}
    ignores = tuple(numbering[i] for i in ignores)
    if len(ignores) > 20:
        ignores = set(ignores)

    if reserved_map:
        if ignores:

            def run_lexer(filename: str, text: str):
                yield Token(0, 0, 0, filename, BOF, "")
                yield from (token for token in lexing(
                    filename, text, table, reserved_map)
                            if token.idint not in ignores)
                yield Token(0, 0, 0, filename, EOF, "")

        else:

            def run_lexer(filename: str, text: str):
                yield Token(0, 0, 0, filename, BOF, "")
                yield from lexing(filename, text, table, reserved_map)
                yield Token(0, 0, 0, filename, EOF, "")

    else:
        if ignores:

            def run_lexer(filename: str, text: str):
                yield Token(0, 0, 0, filename, BOF, "")
                yield from (token for token in lexing_no_reverse(
                    filename, text, table)
                            if token.idint not in ignores)
                yield Token(0, 0, 0, filename, EOF, "")

        else:

            def run_lexer(filename: str, text: str):
                yield Token(0, 0, 0, filename, BOF, "")
                yield from lexing_no_reverse(filename, text, table)
                yield Token(0, 0, 0, filename, EOF, "")

    return numbering, run_lexer
