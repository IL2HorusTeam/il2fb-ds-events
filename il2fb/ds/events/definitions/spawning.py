from dataclasses import dataclass

from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import HumanAircraftActor

from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin
from .mixins import PositionMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class HumanAircraftSpawnedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "weapons", "fuel"]

  actor:   HumanAircraftActor
  weapons: str
  fuel:    int  # as percent, %


@export
@dataclass(frozen=True)
class HumanAircraftDespawnedInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor"]

  actor: HumanAircraftActor


@export
@dataclass(frozen=True)
class AIAircraftDespawnedInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor"]

  actor: AIAircraftActor


@export
@dataclass(frozen=True)
class SpawningEvent(Event):
  category = "spawning"


@export
@register
@dataclass(frozen=True)
class HumanAircraftSpawnedEvent(SpawningEvent):
  verbose_name = _("Human aircraft spawned")
  data: HumanAircraftSpawnedInfo


@export
@register
@dataclass(frozen=True)
class HumanAircraftDespawnedEvent(SpawningEvent):
  verbose_name = _("Human aircraft despawned")
  data: HumanAircraftDespawnedInfo


@export
@register
@dataclass(frozen=True)
class AIAircraftDespawnedEvent(SpawningEvent):
  verbose_name = _("AI aircraft despawned")
  data: AIAircraftDespawnedInfo
