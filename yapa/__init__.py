from yapa.expectations import StrExpectation


def expect(actual: str) -> StrExpectation:
    if isinstance(actual, str):
        return StrExpectation(actual=actual)
    raise NotImplementedError


__all__ = [
    "expect",
]
