from typing import Type, Any

from .base_assertion import BaseAssertion
from yapc.flags import StrFlags


class StrAssertion(BaseAssertion):
    def __init__(self, actual: str, flag_class: Type[StrFlags]):
        return super().__init__(actual, flag_class)

    def __call__(self, dest: str):
        if self.flags.have:
            assert (dest in self.actual) is self.flags.tobe
            return self
        assert (dest == self.actual) is self.flags.tobe
        return self

    def string(self, dest: str) -> "StrAssertion":
        return self(dest=dest)

    def str(self, dest: str) -> "StrAssertion":
        return self(dest=dest)

    def ok(self) -> "StrAssertion":
        assert self.actual if self.flags.tobe else not self.actual
        return self

    def equal(self, dest: Any) -> "StrAssertion":
        assert (self.actual == dest) == self.actual
        return self
