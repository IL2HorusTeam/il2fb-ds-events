from typing import Protocol
from typing import runtime_checkable
from typing import Text


@runtime_checkable
class SupportsText(Protocol):

  def __str__(self) -> Text:
    ...
