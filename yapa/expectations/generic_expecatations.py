from typing import Any

from yapa.impl.assertions.generic_assertion import GenericAssertionImplement


class GenericExpectation:
    impl_class = GenericAssertionImplement

    def __init__(self, actual: Any):
        self.actual = actual

    def to_be(self, target: Any):
        self.impl_class.impl_to_be_equal(self.actual, target=target)
        return self

    def to_contain(self, target: Any):
        self.impl_class.impl_to_contain(self.actual, target=target)
        return self

    def to_be_truthy(self):
        self.impl_class.impl_to_be_truthy(self.actual)
        return self

    def to_be_identical_to(self, target: Any):
        self.impl_class.impl_to_be_identical(self.actual, target)
        return self

    def to_be_length_of(self, target: int):
        self.impl_class.impl_to_be_length_of(self.actual, target)
        return self
