from __future__ import annotations

from typing import TypeVar, Type, Dict, cast, Self
from abc import ABC


class Injectable(ABC):

    def __init__(self) -> None:
        pass

    @classmethod
    @property
    def Instance(cls) -> Self:
        return InjectionManager.get_or_create(cls)


T = TypeVar("T", bound=Injectable)


class InjectionManager:

    _instances: Dict[Type[Injectable], Injectable] = dict()

    @classmethod
    def get_or_create(cls, _type: Type[T]) -> T:

        if not issubclass(_type, Injectable):
            raise TypeError(f"{_type} is not a subclass of Injectable")

        if _type not in cls._instances:
            cls._instances[_type] = _type()

        return cast(T, cls._instances[_type])


def Inject(_type: Type[T]) -> T:
    return InjectionManager.get_or_create(_type)
