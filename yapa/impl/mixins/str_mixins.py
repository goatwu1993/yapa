class LowerCaseMixin:
    @staticmethod
    def impl_to_be_lower_case(source: str) -> None:
        assert source == source.lower()


class UpperCaseMixin:
    @staticmethod
    def impl_to_be_upper_case(source: str) -> None:
        assert source == source.upper()
