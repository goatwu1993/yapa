from typing import Type

from .base_assertion import BaseAssertion
from yapc.flags import StrFlags


class StrAssertion(BaseAssertion):
    def __init__(self, actual: str, flag_class: Type[StrFlags]):
        self._actual = actual
        self.flags = flag_class()

    def str(self, dest: str) -> "StrAssertion":
        if self.flags.have:
            assert (dest in self.actual) is self.flags.tobe
            return self
        assert (dest == self.actual) is self.flags.tobe
        return self

    def string(self, dest: str) -> "StrAssertion":
        return self.str(dest=dest)
