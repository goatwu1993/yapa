from typing import Union
from yapc.impl.assertions import StringAssertion


def expect(
    actual: str,
) -> StringAssertion:
    if isinstance(actual, str):
        return StringAssertion(StringAssertionsImpl(actual._impl_obj))
    raise ValueError(f"Unsupported type: {type(actual)}")


__all__ = [
    "expect",
]