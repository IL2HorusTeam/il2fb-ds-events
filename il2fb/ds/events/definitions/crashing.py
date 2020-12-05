from dataclasses import dataclass

from il2fb.commons.actors import Actor
from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import MovingUnitActor
from il2fb.commons.actors import MovingUnitMemberActor
from il2fb.commons.actors import StationaryUnitActor
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
class CrashingInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", ]

  actor: Actor


@export
@dataclass(frozen=True)
class AIAircraftCrashedInfo(CrashingInfo):
  actor: AIAircraftActor


@export
@dataclass(frozen=True)
class HumanAircraftCrashedInfo(CrashingInfo):
  actor: HumanAircraftActor


@export
@dataclass(frozen=True)
class MovingUnitCrashedInfo(CrashingInfo):
  actor: MovingUnitActor


@export
@dataclass(frozen=True)
class MovingUnitMemberCrashedInfo(CrashingInfo):
  actor: MovingUnitMemberActor


@export
@dataclass(frozen=True)
class StationaryUnitCrashedInfo(CrashingInfo):
  actor: StationaryUnitActor


@export
@dataclass(frozen=True)
class UnknownActorCrashedInfo(CrashingInfo):
  actor: UnknownActor


@export
@dataclass(frozen=True)
class CrashingEvent(Event):
  category = "crashing"


@export
@register
@dataclass(frozen=True)
class AIAircraftCrashedEvent(CrashingEvent):
  verbose_name = _("AI aircraft crashed")
  data: AIAircraftCrashedInfo


@export
@register
@dataclass(frozen=True)
class HumanAircraftCrashedEvent(CrashingEvent):
  verbose_name = _("Human aircraft crashed")
  data: HumanAircraftCrashedInfo


@export
@register
@dataclass(frozen=True)
class MovingUnitCrashedEvent(CrashingEvent):
  verbose_name = _("Moving unit crashed")
  data: MovingUnitCrashedInfo


@export
@register
@dataclass(frozen=True)
class MovingUnitMemberCrashedEvent(CrashingEvent):
  verbose_name = _("Moving unit member crashed")
  data: MovingUnitMemberCrashedInfo


@export
@register
@dataclass(frozen=True)
class StationaryUnitCrashedEvent(CrashingEvent):
  verbose_name = _("Stationary unit crashed")
  data: StationaryUnitCrashedInfo


@export
@register
@dataclass(frozen=True)
class UnknownActorCrashedEvent(CrashingEvent):
  verbose_name = _("Unknown actor crashed")
  data: UnknownActorCrashedInfo
