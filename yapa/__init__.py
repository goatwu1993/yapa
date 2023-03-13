from typing import Union, overload
from yapa.impl.assertions import StrAssertion, DictAssertion, BoolAssertion
from yapa.flags import StrFlags, BoolFlags


@overload
def expect(actual: str) -> StrAssertion:
    ...


@overload
def expect(actual: bool) -> BoolAssertion:
    ...


@overload
def expect(actual: dict) -> DictAssertion:
    ...


def expect(
    actual: Union[str, dict, bool],
) -> Union[StrAssertion, DictAssertion, BoolAssertion]:
    if isinstance(actual, str):
        return StrAssertion(actual=actual, flag_class=StrFlags)
    if isinstance(actual, bool):
        return BoolAssertion(actual=actual, flag_class=BoolFlags)
    raise NotImplementedError


__all__ = [
    "expect",
]
