from dataclasses import dataclass

from .actors import HumanActor
from .base import Event
from .mixins import PrimitiveDataclassMixin
from .registry import register
from .utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class SimpleChatMessage(PrimitiveDataclassMixin):
  msg: str


@export
@dataclass(frozen=True)
class HumanChatMessage(SimpleChatMessage):
  actor: HumanActor


@export
@dataclass(frozen=True)
class ChatMessageEvent(Event):
  category = "chat"


@export
@register
@dataclass(frozen=True)
class ServerChatMessageEvent(ChatMessageEvent):
  data: SimpleChatMessage
  verbose_name = _("Chat message from server")


@export
@register
@dataclass(frozen=True)
class SystemChatMessageEvent(ChatMessageEvent):
  data: SimpleChatMessage
  verbose_name = _("Chat message from system")


@export
@register
@dataclass(frozen=True)
class HumanChatMessageEvent(ChatMessageEvent):
  data: HumanChatMessage
  verbose_name = _("Chat message from human")
