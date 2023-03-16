from .generic_assertion import GenericAssertionImplement


class StrAssertion(GenericAssertionImplement):
    @staticmethod
    def impl_to_be_lowered(source: str) -> None:
        assert source == source.lower()
