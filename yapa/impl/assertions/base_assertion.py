from typing import Type
from abc import ABC, abstractmethod, abstractproperty


class BaseAssertion(ABC):
    @abstractproperty
    def to(self):
        ...

    @abstractproperty
    def be(self):
        ...

    @abstractproperty
    def have(self):
        ...

    @abstractproperty
    def _not(self):
        ...

    @abstractproperty
    def _and(self):
        ...

    @abstractmethod
    def ok(self):
        ...

    @abstractmethod
    def eql(self):
        ...

    @abstractmethod
    def equal(self):
        ...

    @abstractmethod
    def a(self, dest_class: Type):
        ...

    @abstractmethod
    def an(self, dest_class: Type):
        ...

    @abstractmethod
    def true(self):
        ...

    @abstractmethod
    def false(self):
        ...

    @abstractmethod
    def empty(self):
        ...
