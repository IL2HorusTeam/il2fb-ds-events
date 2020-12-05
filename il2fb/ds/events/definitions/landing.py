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
class LandingInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", ]

  actor: Actor


@export
@dataclass(frozen=True)
class HumanAircraftLandedInfo(LandingInfo):
  actor: HumanAircraftActor


@export
@dataclass(frozen=True)
class AIAircraftLandedInfo(LandingInfo):
  actor: AIAircraftActor


@export
@dataclass(frozen=True)
class UnknownActorLandedInfo(LandingInfo):
  actor: UnknownActor


@export
@dataclass(frozen=True)
class LandingEvent(Event):
  category = "landing"


@export
@register
@dataclass(frozen=True)
class HumanAircraftLandedEvent(LandingEvent):
  verbose_name = _("Human aircraft landed")
  data: HumanAircraftLandedInfo


@export
@register
@dataclass(frozen=True)
class AIAircraftLandedEvent(LandingEvent):
  verbose_name = _("AI aircraft landed")
  data: AIAircraftLandedInfo


@export
@register
@dataclass(frozen=True)
class UnknownActorLandedEvent(LandingEvent):
  verbose_name = _("Unknown actor landed")
  data: UnknownActorLandedInfo
