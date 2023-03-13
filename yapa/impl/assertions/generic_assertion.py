from typing import Any, Type

from .base_assertion_implement_interface import BaseAssertionImplementInterface


class GenericAssertionImplement(BaseAssertionImplementInterface):
    @staticmethod
    def impl_to_have(source: Any, target: Any) -> None:
        assert source in target

    @staticmethod
    def impl_to_be_truthy(source: Any) -> None:
        assert bool(source)

    @staticmethod
    def impl_to_be_identical(source: Any, target: Any) -> None:
        assert id(source) == id(target)

    @staticmethod
    def impl_to_be_equal(source: Any, target: Any) -> None:
        assert source == target

    @staticmethod
    def impl_to_be_class(source: Any, target: Type) -> None:
        assert isinstance(source, target)
