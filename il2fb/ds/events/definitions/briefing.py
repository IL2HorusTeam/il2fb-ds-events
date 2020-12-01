from dataclasses import dataclass

from il2fb.commons.actors import HumanActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event
from .mixins import TimeMixin
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class HumanReturnedToBriefingInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", ]

  actor: HumanActor


@export
@register
@dataclass(frozen=True)
class HumanReturnedToBriefingEvent(Event):
  category = "briefing"
  verbose_name = _("Human returned to briefing")
  data: HumanReturnedToBriefingInfo
