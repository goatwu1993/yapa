from yapa.impl.assertions import StrAssertion

from .generic_expecatations import GenericExpectation


class StrExpectation(GenericExpectation):
    impl_class = StrAssertion

    def __init__(self, actual):
        self.actual = actual

    def to_be_lower_case(self):
        self.impl_class.impl_to_be_lower_case(self.actual)
        return self

    def to_be_upper_case(self):
        self.impl_class.impl_to_be_upper_case(self.actual)
        return self
