from ..mixins.generic_mixins import (
    ContainMixin,
    EqualMixin,
    IdenticalMixin,
    IsInstanceMixin,
    TruthyMixin,
)
from .base_assertion_implement_interface import BaseAssertionImplementInterface


class GenericAssertionImplement(
    BaseAssertionImplementInterface,
    ContainMixin,
    EqualMixin,
    IdenticalMixin,
    TruthyMixin,
    IsInstanceMixin,
):
    pass
