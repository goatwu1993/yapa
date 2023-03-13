from typing import Type, Any
from yapa.flags import BaseFlags
from .base_assertion import BaseAssertion


class GenericAssertion(BaseAssertion):
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

    def ok(self):
        assert bool(self.actual) is self.flags.tobe
        return self

    def eql(self, dest: Any):
        assert (self.actual == dest) == self.flags.tobe
        return self

    def equal(self, dest: Any):
        assert (id(self.actual) == id(dest)) == self.flags.tobe
        return self

    def a(self, dest_class: Type):
        assert isinstance(self.actual, dest_class) == self.flags.tobe
        return self

    def an(self, dest_class: Type):
        return self.a(dest_class=dest_class)

    def true(self):
        assert self.actual is self.actual.tobe
        return self

    def false(self):
        self.flags.tobe = False
        return self.true

    def empty(self):
        assert (len(self.actual) == 0) == self.flags.tobe
        return self
