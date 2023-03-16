from .generic_assertion import GenericAssertionImplement


class StrAssertion(GenericAssertionImplement):
    @staticmethod
    def impl_to_be_lower_case(source: str) -> None:
        assert source == source.lower()

    @staticmethod
    def impl_to_be_upper_case(source: str) -> None:
        assert source == source.upper()
