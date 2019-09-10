from .utils import InternedString
from .token import Token
from warnings import warn
import re
import abc
import typing as t

__all__ = ['Lexer', 'LexerDescriptor', 'RegexLexerDescriptor', 'LiteralLexerDescriptor', 'lexer_reduce', 'lexing']
Lexer = t.Callable[[str, int], t.Optional[t.Tuple[int, str]]]


class LexerDescriptor(abc.ABC):
    typeid: int

    @abc.abstractmethod
    def to_lexer(self) -> Lexer:
        return self.to_lexer()


class RegexLexerDescriptor(LexerDescriptor):

    def __init__(self, typeid: int, regex_pat: str):
        self.typeid = typeid
        self.contents = regex_pat

    def to_lexer(self):
        match = re.compile(self.contents).match
        typeid = self.typeid
        box = InternedString

        def lex(string, pos):
            m = match(string, pos)
            if m:
                return box(m.group())

        return typeid, lex


class LiteralLexerDescriptor(LexerDescriptor):

    def __init__(self, typeid: int, *string_pats: str):
        assert string_pats
        self.typeid = typeid
        self.contents = string_pats

    def to_lexer(self):
        pats = self.contents
        typeid = self.typeid
        make_interned = InternedString
        if len(pats) is 1:
            pats = pats[0]

            def lex(string: str, pos):
                if string.startswith(pats, pos):
                    return make_interned(pats, typeid)
        else:
            def lex(string: str, pos):
                for pat in pats:
                    if string.startswith(pat, pos):
                        return make_interned(pat, typeid)

        return typeid, lex


def lexer_reduce(lexer_descriptors: t.List[LexerDescriptor]) -> t.List[LexerDescriptor]:
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
            contents = sum(tuple(each.contents for each in descriptors), ())

            ret.append(LiteralLexerDescriptor(typeid, *contents))

    return ret


def lexing(filename: str, text: str, lexer_table: list, reserved_map: dict):
    text_length = len(text)
    colno = 0
    lineno = 0
    pos = 0
    newline = '\n'

    while True:
        if text_length <= pos:
            break

        for typeid, case in lexer_table:
            interned_string: InternedString = case(text, pos)

            if interned_string is None:
                continue
            pat = interned_string.s
            casted_typeid = reserved_map.get(pat)
            if casted_typeid is None:
                yield Token(pos, lineno, colno, filename, typeid, interned_string)
            else:
                yield Token(pos, lineno, colno, filename, casted_typeid, interned_string.as_interned())
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
            interned_string = InternedString(ch)
            yield Token(pos, lineno, colno, filename, 0, interned_string)
            if ch == "\n":
                lineno += 1
                colno = 0
            pos += 1
