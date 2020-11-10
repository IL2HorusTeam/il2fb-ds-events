from typing import Protocol
from typing import runtime_checkable
from typing import TypeVar


@runtime_checkable
class SupportsString(Protocol):

  def __str__(self) -> str:
    ...


Event = TypeVar("Event")
