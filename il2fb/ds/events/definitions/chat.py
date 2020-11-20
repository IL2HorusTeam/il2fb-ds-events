from dataclasses import dataclass

from il2fb.commons.actors import HumanActor
from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event
from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class ChatMessage(PrimitiveDataclassMixin):
  __slots__ = ["msg", ]

  msg: str


@export
@dataclass(frozen=True)
class HumanChatMessage(ChatMessage):
  __slots__ = ChatMessage.__slots__ + ["msg", ]

  actor: HumanActor


@export
@dataclass(frozen=True)
class ChatMessageEvent(Event):
  category = "chat"
  data: ChatMessage


@export
@register
@dataclass(frozen=True)
class ServerChatMessageEvent(ChatMessageEvent):
  verbose_name = _("Chat message from server")


@export
@register
@dataclass(frozen=True)
class SystemChatMessageEvent(ChatMessageEvent):
  verbose_name = _("Chat message from system")


@export
@register
@dataclass(frozen=True)
class HumanChatMessageEvent(ChatMessageEvent):
  verbose_name = _("Chat message from human")
  data: HumanChatMessage
