import datetime
import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from dataclasses import dataclass

from typing import Any
from typing import Optional
from typing import TypeVar

from il2fb.commons.actors import HumanActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event
from .mixins import TimeMixin
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


HumanToggledRecordingInfo = TypeVar("HumanToggledRecordingInfo")


@export
@dataclass(frozen=True)
class HumanToggledRecordingInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", "state", ]

  actor: Optional[HumanActor]
  state: bool

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> HumanToggledRecordingInfo:
    """
    Override base method to handle 'Optional' fields.

    """
    actor = value['actor']
    if actor:
      actor = HumanActor.from_primitive(actor)

    timestamp = datetime.time.fromisoformat(value['timestamp'])

    return cls(
      timestamp=timestamp,
      state=value['state'],
      actor=actor,
    )


@export
@register
@dataclass(frozen=True)
class HumanToggledRecordingEvent(Event):
  category = "recording"
  verbose_name = _("Human toggled track recording")
  data: HumanToggledRecordingInfo
