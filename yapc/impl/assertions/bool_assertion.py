from typing import Any
from .base_assertion import BaseAssertion


class BoolAssertion(BaseAssertion):
    def ok(self) -> "BoolAssertion":
        assert self.actual is self.flags.tobe
        return self

    def equal(self, dest: Any) -> "BoolAssertion":
        assert (self.actual == dest) == self.flags.tobe
        return self