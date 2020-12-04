from dataclasses import dataclass

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
class LandingInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", ]


@export
@dataclass(frozen=True)
class HumanAircraftLandedInfo(LandingInfo):
  __slots__ = LandingInfo.__slots__ + ["actor", ]

  actor: HumanAircraftActor


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
