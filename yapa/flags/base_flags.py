from dataclasses import dataclass


@dataclass
class BaseFlags:
    have: bool = False
    tobe: bool = True
