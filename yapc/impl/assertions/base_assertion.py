from typing import Type, Any
from yapc.flags import BaseFlags


class BaseAssertion:
    def __init__(self, actual: Any, flag_class: Type[BaseFlags]):
        self._actual = actual
        self.flag_class = flag_class
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

    @property
    def _and(self):
        self.flags = self.flag_class()
        return self

    def __call__(self, *args, **kwargs):
        ...

    def a(self, dest_class: Type):
        assert isinstance(self.actual, dest_class) == self.flag_class.tobe
        return self

    def an(self, dest_class: Type):
        return self.a(dest_class=dest_class)
