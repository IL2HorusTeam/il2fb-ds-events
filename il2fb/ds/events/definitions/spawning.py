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
class HumanSpawnedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "weapons", "fuel"]

  actor:   HumanAircraftActor
  weapons: str
  fuel:    int  # as percent, %


@export
@dataclass(frozen=True)
class HumanDespawnedInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
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
class HumanSpawnedEvent(SpawningEvent):
  verbose_name = _("Human spawned")
  data: HumanSpawnedInfo


@export
@register
@dataclass(frozen=True)
class HumanDespawnedEvent(SpawningEvent):
  verbose_name = _("Human despawned")
  data: HumanDespawnedInfo


@export
@register
@dataclass(frozen=True)
class AIAircraftDespawnedEvent(SpawningEvent):
  verbose_name = _("AI aircraft despawned")
  data: AIAircraftDespawnedInfo
