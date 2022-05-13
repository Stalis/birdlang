import enum
import re
from typing import Callable


@enum.unique
class TokenType(enum.Enum):
    EOF = (0, None)
    Ident = (0x1, r'[_a-zA-Z][_a-zA-Z0-9]*')
    Directive = (0x2, r'\$[_a-zA-Z][_a-zA-Z0-9]*')
    NewLine = (0x3, r'[\n\r]')
    Whitespace = (0x4, r'\s')
    # Literals
    LiteralStr = (0x10, r'".*"')
    LiteralChar = (0x11, r"'.'")
    LiteralInt = (0x12, r'\d+')
    LiteralFloat = (0x13, r'\d+\.\d*')
    # Symbols
    SymbolAssign = (0x20, r'=')
    SymbolEqual = (0x21, r'==')
    SymbolLess = (0x22, r'<')
    SymbolGreater = (0x23, r'>')
    SymbolLessOrEqual = (0x24, r'<=')
    SymbolGreaterOrEqual = (0x25, r'>=')

    def __init__(self, code: int,
                 pattern_or_checker: str | Callable[[str], bool]) -> None:
        self.code = code
        if isinstance(pattern_or_checker, str):

            def checker(input: str) -> bool:
                re.match(pattern_or_checker, input)

            self.__checker = checker
        else:
            self.__checker = pattern_or_checker

    def check(self, input: str) -> bool:
        return self.__checker(input)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
