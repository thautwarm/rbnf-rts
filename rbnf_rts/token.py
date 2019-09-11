class Token:
    offset: int
    lineno: int
    colno: int
    filename: str
    idint: int
    value: str
    _repr: str
    __slots__ = ('offset', 'lineno', 'colno', 'filename', 'idint', 'value', '_repr')

    def __init__(self, offset, lineno, colno, filename, type, value):
        self.offset = offset
        self.lineno = lineno
        self.colno = colno
        self.filename = filename
        self.idint = type
        self.value = value
        self._repr = None

    def __eq__(self, other: 'Token'):
        if not isinstance(other, Token):
            return False

        return (self.offset == other.offset and self.filename == other.filename
                and self.idint == other.idint and self.value == other.value
                and self.colno == other.colno and self.lineno == other.lineno)

    def __hash__(self):
        return (self.offset ^ self.lineno ^ self.colno + 2333 + self.idint) ^ hash(
            self.filename) ^ hash(self.value)

    def __repr__(self):
        if self._repr is None:
            self._repr = "Token(offset=%d, lineno=%d, colno=%d, filename=%s, type=%d, value=%s)" % (
                self.offset, self.lineno, self.colno, self.filename, self.idint,
                repr(self.value))
        return self._repr
