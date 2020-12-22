import datetime
import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from typing import Any
from typing import TypeVar

from dataclasses import dataclass

from il2fb.commons.structures import PrimitiveDataclassMixin

from il2fb.commons.targets import TARGET_STATES
from il2fb.commons.targets import TargetStateConstant

from .base import Event
from .mixins import TimestampMixin
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


TargetStateChangedInfo = TypeVar('TargetStateChangedInfo')


@export
@dataclass(frozen=True)
class TargetStateChangedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["index", "state", ]

  index: int
  state: TargetStateConstant

  def to_primitive(self, *args, **kwargs) -> Dict[str, Any]:
    """
    Override base method to handle fields with complex constants.

    """
    return {
      'timestamp': self.timestamp.isoformat(),
      'index':     self.index,
      'state':     self.state.name,
    }

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> TargetStateChangedInfo:
    """
    Override base method to handle fields with complex constants.

    """
    timestamp   = datetime.datetime.fromisoformat(value['timestamp'])
    index       = value['index']
    state       = TARGET_STATES[value['state']]

    return cls(
      timestamp=timestamp,
      index=index,
      state=state,
    )


@export
@register
@dataclass(frozen=True)
class TargetStateChangedEvent(Event):
  category = "target"
  verbose_name = _("Target state changed")
  data: TargetStateChangedInfo
