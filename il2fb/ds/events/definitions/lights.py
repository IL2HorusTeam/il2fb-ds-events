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
class HumanToggledLandingLightsInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", "state", ]

  actor: HumanAircraftActor
  state: bool


@export
@register
@dataclass(frozen=True)
class HumanToggledLandingLightsEvent(Event):
  category = "lights"
  verbose_name = _("Human toggled landing lights")
  data: HumanToggledLandingLightsInfo
