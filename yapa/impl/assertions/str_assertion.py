from ..mixins.str_mixins import LowerCaseMixin, UpperCaseMixin
from .generic_assertion import GenericAssertionImplement


class StrAssertion(GenericAssertionImplement, LowerCaseMixin, UpperCaseMixin):
    pass
