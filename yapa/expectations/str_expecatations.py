from yapa.impl.assertions import StrAssertion

from .generic_expecatations import GenericExpectation


class StrExpectation(GenericExpectation):
    impl_class = StrAssertion

    def __init__(self, actual):
        self.actual = actual