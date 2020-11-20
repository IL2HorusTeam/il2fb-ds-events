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


@export
@dataclass(frozen=True)
class ChannelInfo(PrimitiveDataclassMixin):
  __slots__ = ["channel_no", "address", "port", ]

  channel_no: int
  address:    str
  port:       int


@export
@dataclass(frozen=True)
class HumanConnectionStartedInfo(PrimitiveDataclassMixin):
  __slots__ = ["channel_info", ]

  channel_info: ChannelInfo


@export
@dataclass(frozen=True)
class HumanConnectionEstablishedInfo(PrimitiveDataclassMixin):
  __slots__ = ["channel_info", "actor", ]

  channel_info: ChannelInfo
  actor:        HumanActor


@export
@dataclass(frozen=True)
class HumanConnectionEstablishedLightInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["time", "actor", ]

  actor: HumanActor


HumanConnectionLostInfo = TypeVar("HumanConnectionLostInfo")


@export
@dataclass(frozen=True)
class HumanConnectionLostInfo(PrimitiveDataclassMixin):
  __slots__ = ["channel_info", "reason", ]

  channel_info: ChannelInfo
  reason:       Optional[str]

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> HumanConnectionLostInfo:
    """
    Override base method to handle 'Optional' fields.

    """
    return cls(
      channel_info=ChannelInfo.from_primitive(value['channel_info']),
      reason=value['reason'],
    )


@export
@dataclass(frozen=True)
class HumanConnectionLostLightInfo(TimeMixin, PrimitiveDataclassMixin):
  __slots__ = ["time", "actor", ]

  actor: HumanActor


@export
@dataclass(frozen=True)
class HumanConnectionEvent(Event):
  category = "connection"


@export
@register
@dataclass(frozen=True)
class HumanConnectionStartedEvent(HumanConnectionEvent):
  verbose_name = _("Human connection with server started")
  data: HumanConnectionStartedInfo


@export
@register
@dataclass(frozen=True)
class HumanConnectionEstablishedEvent(HumanConnectionEvent):
  verbose_name = _("Human connection with server established")
  data: HumanConnectionEstablishedInfo


@export
@register
@dataclass(frozen=True)
class HumanConnectionEstablishedLightEvent(HumanConnectionEvent):
  verbose_name = _("Human connection with server established (light)")
  data: HumanConnectionEstablishedLightInfo


@export
@register
@dataclass(frozen=True)
class HumanConnectionLostEvent(HumanConnectionEvent):
  verbose_name = _("Human connection with server lost")
  data: HumanConnectionLostInfo


@export
@register
@dataclass(frozen=True)
class HumanConnectionLostLightEvent(HumanConnectionEvent):
  verbose_name = _("Human connection with server lost (light)")
  data: HumanConnectionLostLightInfo
