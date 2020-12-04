from dataclasses import dataclass

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class HumanSpawnedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "weapons", "fuel"]

  actor:   HumanAircraftActor
  weapons: str
  fuel:    int  # as percent, %


@export
@register
@dataclass(frozen=True)
class HumanSpawnedEvent(Event):
  category = "spawning"
  verbose_name = _("Human spawned")
  data: HumanSpawnedInfo
