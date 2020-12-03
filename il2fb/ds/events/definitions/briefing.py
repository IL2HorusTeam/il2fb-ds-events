import datetime
import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from dataclasses import dataclass

from typing import Any
from typing import TypeVar

from il2fb.commons.actors import HumanActor
from il2fb.commons.belligerents import BELLIGERENTS
from il2fb.commons.belligerents import BelligerentConstant
from il2fb.commons.spatial import Point3D
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin
from .mixins import PositionMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class BriefingEvent(Event):
  category = "briefing"


@export
@dataclass(frozen=True)
class HumanReturnedToBriefingInfo(TimestampMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "actor", ]

  actor: HumanActor


@export
@register
@dataclass(frozen=True)
class HumanReturnedToBriefingEvent(BriefingEvent):
  verbose_name = _("Human returned to briefing")
  data: HumanReturnedToBriefingInfo


HumanSelectedAirfieldInfo = TypeVar("HumanSelectedAirfieldInfo")


@export
@dataclass(frozen=True)
class HumanSelectedAirfieldInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "actor", "belligerent", ]

  actor:       HumanActor
  belligerent: BelligerentConstant

  def to_primitive(self, *args, **kwargs) -> Dict[str, Any]:
    """
    Override base method to handle fields with complex constants.

    """
    return {
      'timestamp':   self.timestamp.isoformat(),
      'pos':         self.pos.to_primitive(*args, **kwargs),
      'actor':       self.actor.to_primitive(*args, **kwargs),
      'belligerent': self.belligerent.name,
    }

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> HumanSelectedAirfieldInfo:
    """
    Override base method to handle fields with complex constants.

    """
    timestamp   = datetime.datetime.fromisoformat(value['timestamp'])
    pos         = Point3D.from_primitive(value['pos'], *args, **kwargs)
    actor       = HumanActor.from_primitive(value['actor'], *args, **kwargs)
    belligerent = BELLIGERENTS[value['belligerent']]

    return cls(
      timestamp=timestamp,
      pos=pos,
      actor=actor,
      belligerent=belligerent,
    )


@export
@register
@dataclass(frozen=True)
class HumanSelectedAirfieldEvent(BriefingEvent):
  verbose_name = _("Human selected airfield")
  data: HumanSelectedAirfieldInfo
