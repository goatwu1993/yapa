from typing import Any, Type


class ContainMixin:
    @staticmethod
    def impl_to_contain(source: Any, target: Any) -> None:
        assert target in source


class TruthyMixin:
    @staticmethod
    def impl_to_be_truthy(source: Any) -> None:
        assert bool(source)


class IdenticalMixin:
    @staticmethod
    def impl_to_be_identical(source: Any, target: Any) -> None:
        assert id(source) == id(target)


class EqualMixin:
    @staticmethod
    def impl_to_be_equal(source: Any, target: Any) -> None:
        assert source == target


class IsInstanceMixin:
    @staticmethod
    def impl_to_be_class(source: Any, target: Type) -> None:
        assert isinstance(source, target)
