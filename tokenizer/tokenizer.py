from typing import TextIO
from tokenizer.ioreader import IOReader
import json

from tokenizer.token_type import TokenType


class Token(object):

    def __init__(self,
                 type: TokenType,
                 src: str,
                 pos: int = 0,
                 lineno: int = 0) -> None:
        self.type = type
        self.src = src
        self.pos = pos
        self.lineno = lineno

    def as_tuple(self) -> tuple[str, str]:
        return (self.type.name, self.src)

    def __repr__(self) -> str:
        res = self.__dict__
        res['type'] = res['type'].__repr__()
        return json.dumps(res)


class Tokenizer(object):

    def __init__(self, input: TextIO) -> None:
        self.reader = IOReader(input)
        self.lineno: int = 0
        self.pos: int = 0
        self.EOF: bool = False

    def next_char(self) -> str:
        if self.EOF:
            return ''

        res = self.reader.read()
        if len(res) == 0:
            self.EOF = True

        pos += 1
        return res

    def lookup(self) -> str:
        return self.reader.lookup()

    def new_line(self):
        self.lineno += 1
        self.pos = 0

    def next_token(self) -> Token:
        buf = self.next_char()

        if TokenType.NewLine.check(buf):
            return Token(TokenType.NewLine, buf)
        elif TokenType.Whitespace.check(buf):
            buf1 = buf
            while TokenType.Whitespace.check(buf1):
                buf1 += self.lookup()

        return Token(TokenType.EOF, buf)
