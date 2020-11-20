from dataclasses import dataclass

from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class CheatingInfo(PrimitiveDataclassMixin):
  __slots__ = ["channel_no", "cheat_code", "cheat_details", ]

  channel_no:    int
  cheat_code:    int
  cheat_details: str


@export
@register
@dataclass(frozen=True)
class CheatingDetectedEvent(Event):
  category     = "cheating"
  verbose_name = _("Cheating detected")

  data: CheatingInfo
