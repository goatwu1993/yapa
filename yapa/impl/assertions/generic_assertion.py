from ..mixins.generic_mixins import (
    ContainMixin,
    EqualMixin,
    IdenticalMixin,
    IsInstanceMixin,
    TruthyMixin,
)
from ..mixins.length_mixins import LengthMixin
from .base_assertion_implement_interface import BaseAssertionImplementInterface


class GenericAssertionImplement(
    BaseAssertionImplementInterface,
    ContainMixin,
    EqualMixin,
    IdenticalMixin,
    TruthyMixin,
    IsInstanceMixin,
    LengthMixin,
):
    pass
