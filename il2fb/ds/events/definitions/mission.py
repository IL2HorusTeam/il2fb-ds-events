import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from dataclasses import dataclass
from pathlib import Path

from typing import Any

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
