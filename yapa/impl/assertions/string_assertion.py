from typing import Type

from typing_extensions import Self

from yapa.flags import StrFlags

from .generic_assertion import GenericAssertion


class StrAssertion(GenericAssertion):
    def __init__(self, actual: str, flag_class: Type[StrFlags]):
        return super().__init__(actual, flag_class)

    def __call__(self, dest: str) -> Self:
        if self.flags.have:
            assert (dest in self.actual) is self.flags.tobe
            return self
        assert (dest == self.actual) is self.flags.tobe
        return self

    def string(self, dest: str) -> Self:
        self(dest=dest)
        return self

    def str(self, dest: str) -> Self:
        self(dest=dest)
        return self
