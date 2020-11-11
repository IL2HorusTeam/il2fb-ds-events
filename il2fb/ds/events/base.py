import sys

from dataclasses import dataclass
from dataclasses import field

if sys.version_info < (3, 9):
  from typing import Container
else:
  from collections.abc import Container

from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Optional

from .lang import classproperty_readonly

from .mixins import PrimitiveDataclassMixin
from .mixins import VerboseDataclassMixin

from .utils import export


@export
@dataclass(frozen=True)
class EventBase(PrimitiveDataclassMixin):
  # TODO: move to commons?
  ...


@export
@dataclass(frozen=True)
class Event(VerboseDataclassMixin, EventBase):
  data:     Any
  category: ClassVar[str] = field(init=False)  # Must be overriden by derived classes

  @classproperty_readonly
  def name(cls) -> str:
    return cls.__name__

  def to_primitive(self, excludes: Optional[Container[str]] = None) -> Dict[str, Any]:
    result = super().to_primitive(excludes)
    result['name'] = self.name
    return result
