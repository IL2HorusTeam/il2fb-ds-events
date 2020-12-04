from dataclasses import dataclass

from il2fb.commons.actors import HumanActor
from il2fb.commons.actors import HumanAircraftCrewMemberActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin
from .mixins import PositionMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class HumanOccupiedCrewMemberSeatInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", ]

  actor:  HumanActor
  target: HumanAircraftCrewMemberActor


@export
@register
@dataclass(frozen=True)
class HumanOccupiedCrewMemberSeatEvent(Event):
  category = "seats"
  verbose_name = _("Human occupied crew member seat")
  data: HumanOccupiedCrewMemberSeatInfo
