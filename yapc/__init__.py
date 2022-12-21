from typing import Union, overload
from yapc.impl.assertions import StrAssertion, DictAssertion
from yapc.flags import StrFlags


@overload
def expect(actual: str) -> StrAssertion:
    ...


@overload
def expect(actual: dict) -> DictAssertion:
    ...


def expect(
    actual: Union[str, dict],
) -> Union[StrAssertion, DictAssertion]:
    if isinstance(actual, str):
        return StrAssertion(actual=actual, flag_class=StrFlags)
    raise NotImplementedError


__all__ = [
    "expect",
]