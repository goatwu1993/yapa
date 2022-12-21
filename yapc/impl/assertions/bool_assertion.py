from .base_assertion import BaseAssertion


class BoolAssertion(BaseAssertion):
    def ok(self):
        assert self.actual is self.flags.tobe