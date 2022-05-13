from queue import SimpleQueue
from typing import TextIO


class IOReader(object):

    def __init__(self, input: TextIO) -> None:
        self.__io = input
        self.__lookup_buf = SimpleQueue()
        self.__pos = 0

    def read(self, n=1) -> str:
        res = self._drain_lookup(n)
        if len(res) < n:
            res += self.__io.read(n - len(res))

        return res

    def lookup(self) -> str:
        ch = self.__io.read(1)
        self.__lookup_buf.append(ch)
        return ch

    def _drain_lookup(self, n=1) -> str:
        res = ''
        while not self.__lookup_buf.empty() and len(res) < n:
            res += self.__lookup_buf.get()
            self.__pos += 1

        return res
