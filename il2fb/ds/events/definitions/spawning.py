from dataclasses import dataclass

from il2fb.commons.actors import Actor
from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import UnknownActor

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
class DespawningInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", ]

  actor: Actor


@export
@dataclass(frozen=True)
class HumanAircraftDespawnedInfo(DespawningInfo):
  actor: HumanAircraftActor


@export
@dataclass(frozen=True)
class AIAircraftDespawnedInfo(DespawningInfo):
  actor: AIAircraftActor


@export
@dataclass(frozen=True)
class UnknownActorDespawnedInfo(DespawningInfo):
  actor: UnknownActor


@export
@dataclass(frozen=True)
class SpawningEvent(Event):
  category = "spawn"


@export
@register
@dataclass(frozen=True)
class HumanAircraftSpawnedEvent(SpawningEvent):
  verbose_name = _("Human aircraft spawned")
  data: HumanAircraftSpawnedInfo


@export
@dataclass(frozen=True)
class DespawningEvent(Event):
  category = "despawn"


@export
@register
@dataclass(frozen=True)
class HumanAircraftDespawnedEvent(DespawningEvent):
  verbose_name = _("Human aircraft despawned")
  data: HumanAircraftDespawnedInfo


@export
@register
@dataclass(frozen=True)
class AIAircraftDespawnedEvent(DespawningEvent):
  verbose_name = _("AI aircraft despawned")
  data: AIAircraftDespawnedInfo


@export
@register
@dataclass(frozen=True)
class UnknownActorDespawnedEvent(DespawningEvent):
  verbose_name = _("Unknown actor despawned")
  data: UnknownActorDespawnedInfo
