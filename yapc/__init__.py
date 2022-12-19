from typing import Union, overload
from yapc.impl.assertions import StringAssertion, DictAssertion


@overload
def expect(actual: str) -> StringAssertion:
    ...


@overload
def expect(actual: dict) -> DictAssertion:
    ...


def expect(
    actual: Union[str, dict],
) -> StringAssertion:
    if isinstance(actual, str):
        return StringAssertion(StringAssertionsImpl(actual._impl_obj))
    if isinstance(actual, str):
        return DictAssertion(StringAssertionsImpl(actual._impl_obj))
    raise ValueError(f"Unsupported type: {type(actual)}")


__all__ = [
    "expect",
]