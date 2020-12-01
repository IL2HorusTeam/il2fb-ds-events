from dataclasses import dataclass

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event
from .mixins import TimeMixin
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class HumanToggledWingtipSmokesInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "state", ]

  actor: HumanAircraftActor
  state: bool


@export
@register
@dataclass(frozen=True)
class HumanToggledWingtipSmokesEvent(Event):
  category = "smokes"
  verbose_name = _("Human toggled wingtip smokes")
  data: HumanToggledWingtipSmokesInfo
