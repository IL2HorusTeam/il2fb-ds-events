from dataclasses import dataclass

from .mixins import PrimitiveDataclassMixin
from .utils import export


@export
@dataclass(frozen=True)
class Actor(PrimitiveDataclassMixin):
  ...


@export
@dataclass(frozen=True)
class HumanActor(Actor):
  callsign: str
