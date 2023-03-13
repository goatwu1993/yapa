from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Type

from typing_extensions import Self


class BaseAssertionInterface(ABC):
    @abstractproperty
    def to(self) -> Self:
        ...

    @abstractproperty
    def be(self) -> Self:
        ...

    @abstractproperty
    def have(self) -> Self:
        ...

    @abstractproperty
    def _not(self) -> Self:
        ...

    @abstractmethod
    def ok(self) -> Self:
        ...

    @abstractmethod
    def eql(self, dest: Any):
        ...

    @abstractmethod
    def equal(self, dest: Any) -> Self:
        ...

    @abstractmethod
    def a(self, dest_class: Type) -> Self:
        ...

    @abstractmethod
    def an(self, dest_class: Type) -> Self:
        ...
