import datetime
import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from dataclasses import dataclass
from pathlib import Path

from typing import Any
from typing import TypeVar

from il2fb.commons.belligerents import BELLIGERENTS
from il2fb.commons.belligerents import BelligerentConstant

from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class MissionLoadedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "file_path", ]

  file_path: Path

  def to_primitive(self, *args, **kwargs) -> Dict[str, Any]:
    return {
      "timestamp": self.timestamp.isoformat(),
      "file_path": str(self.file_path),
    }


@export
@dataclass(frozen=True)
class MissionStartedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", ]


@export
@dataclass(frozen=True)
class MissionEndedInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", ]


MissionWonInfo = TypeVar('MissionWonInfo')

@export
@dataclass(frozen=True)
class MissionWonInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "belligerent", ]

  belligerent: BelligerentConstant

  def to_primitive(self, *args, **kwargs) -> Dict[str, Any]:
    """
    Override base method to handle fields with complex constants.

    """
    return {
      'timestamp':   self.timestamp.isoformat(),
      'belligerent': self.belligerent.name,
    }

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> MissionWonInfo:
    """
    Override base method to handle fields with complex constants.

    """
    timestamp   = datetime.datetime.fromisoformat(value['timestamp'])
    belligerent = BELLIGERENTS[value['belligerent']]

    return cls(
      timestamp=timestamp,
      belligerent=belligerent,
    )


@export
@dataclass(frozen=True)
class MissionStatusEvent(Event):
  category = "mission"


@export
@register
@dataclass(frozen=True)
class MissionLoadedEvent(MissionStatusEvent):
  verbose_name = _("Mission loaded")
  data: MissionLoadedInfo


@export
@register
@dataclass(frozen=True)
class MissionStartedEvent(MissionStatusEvent):
  verbose_name = _("Mission started")
  data: MissionStartedInfo


@export
@register
@dataclass(frozen=True)
class MissionEndedEvent(MissionStatusEvent):
  verbose_name = _("Mission ended")
  data: MissionEndedInfo


@export
@register
@dataclass(frozen=True)
class MissionWonEvent(MissionStatusEvent):
  verbose_name = _("Mission won")
  data: MissionWonInfo
