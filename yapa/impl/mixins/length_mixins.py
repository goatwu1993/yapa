from typing import Any


class LengthMixin:
    @staticmethod
    def impl_to_be_length_of(source: Any, target: int):
        assert len(source) == target
