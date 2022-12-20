from typing import Type, Any
from yapc.flags import BaseFlags


class BaseAssertion:
    def __init__(self, actual: Any, flag_class: Type[BaseFlags]):
        self._actual = actual
        self.flags = flag_class()

    @property
    def to(self):
        return self

    @property
    def be(self):
        return self

    @property
    def have(self):
        self.flags.have = True
        return self

    @property
    def actual(self):
        return self._actual

    @property
    def _not(self):
        self.flags.tobe = False
        return self
