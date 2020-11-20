import sys

if sys.version_info >= (3, 9):
  from collections.abc import Container

  Dict = dict

else:
  from typing import Container
  from typing import Dict

from dataclasses import dataclass
from dataclasses import field

from typing import Any
from typing import ClassVar
from typing import Optional

from il2fb.commons.structures import PrimitiveDataclassMixin
from il2fb.commons.structures import VerboseDataclassMixin

from ._lang import classproperty_readonly
from ._utils import export


@export
@dataclass(frozen=True)
class EventBase(PrimitiveDataclassMixin):
  ...


@export
@dataclass(frozen=True)
class Event(VerboseDataclassMixin, EventBase):
  __slots__ = ["data", ]

  data:     Any
  category: ClassVar[str] = field(init=False)  # Must be overriden by derived classes

  @classproperty_readonly
  def name(cls) -> str:
    return cls.__name__

  def to_primitive(
    self,
    excludes: Optional[Container[str]] = None,
    *args,
    **kwargs
  ) -> Dict[str, Any]:

    result = super().to_primitive(excludes=excludes, *args, **kwargs)
    result['name'] = self.name
    return result
