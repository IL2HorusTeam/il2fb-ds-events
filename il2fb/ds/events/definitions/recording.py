import datetime

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
class HumanToggledRecordingInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "state", ]

  actor: HumanActor
  state: bool


@export
@register
@dataclass(frozen=True)
class HumanToggledRecordingEvent(Event):
  category = "recording"
  verbose_name = _("Human toggled track recording")
  data: HumanToggledRecordingInfo
