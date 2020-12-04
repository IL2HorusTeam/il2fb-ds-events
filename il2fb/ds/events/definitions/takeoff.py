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
class HumanAircraftTookOffInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", ]

  actor: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftTookOffEvent(Event):
  category = "take-off"
  verbose_name = _("Human aircraft took-off")
  data: HumanAircraftTookOffInfo
