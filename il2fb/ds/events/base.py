from dataclasses import dataclass
from dataclasses import field

from typing import Any
from typing import Container
from typing import Dict
from typing import Optional
from typing import Text

from .mixins import PrimitiveDataclassMixin
from .mixins import VerboseDataclassMixin

from .typing import SupportsText
from .utils import export


@dataclass(frozen=True)
class EventBase:
  line:     Text
  data:     Any
  category: Text = field(init=False)
  src:      Text = field(init=False)


@export
@dataclass(frozen=True)
class Event(PrimitiveDataclassMixin, VerboseDataclassMixin, EventBase):

  @property
  def name(self) -> Text:
    return self.__class__.__name__

  def to_primitive(self, excludes: Optional[Container] = None) -> Dict[Text, Any]:
    result = super().to_primitive(excludes)
    result['name'] = self.name
    return result


@export
@dataclass(frozen=True)
class ConsoleEvent(Event):
  src: Text = field(default="console", init=False)


@export
@dataclass(frozen=True)
class GameLogEvent(Event):
  src: Text = field(default="gamelog", init=False)
