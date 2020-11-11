import dataclasses

from typing import Any
from typing import ClassVar
from typing import Container
from typing import Dict
from typing import Optional

from .typing import SupportsString
from .utils import export


@export
@dataclasses.dataclass(frozen=True)
class VerboseDataclassMixin:
  # TODO: move to commons?
  verbose_name: ClassVar[SupportsString] = dataclasses.field(
    init=False,
  )
  help_text: ClassVar[Optional[SupportsString]] = dataclasses.field(
    init=False,
    # default=None,
  )


@export
class PrimitiveDataclassMixin:
  # TODO: move to commons?

  def to_primitive(self, excludes: Optional[Container] = None) -> Dict[str, Any]:
    return {
      key: self._value_to_primitive(
        value=getattr(self, key),
        excludes=excludes,
      )
      for key in self.__dataclass_fields__.keys()
      if (not excludes) or (key not in excludes)
    }

  @staticmethod
  def _value_to_primitive(value: Any, excludes: Optional[Container] = None) -> Any:
    if value is None:
      return

    if hasattr(value, "to_primitive"):
      return value.to_primitive(excludes=excludes)

    if hasattr(value, "isoformat"):
      return value.isoformat()

    if isinstance(value, SupportsString) and not isinstance(value, str):
      return str(value)

    return value

  @classmethod
  def from_primitive(cls, value: Dict[str, Any]) -> Any:
    kwargs = {
      key: cls._value_from_primitive(
        value=value[key],
        type_=field.type,
      )
      for key, field in cls.__dataclass_fields__.items()
      if field.init
    }
    return cls(**kwargs)

  @staticmethod
  def _value_from_primitive(value: Any, type_: type) -> Any:
    if value is None:
      return

    if isinstance(value, type_):
      return value

    fromisoformat = getattr(type_, "fromisoformat", None)
    if fromisoformat:
      return fromisoformat(value)

    from_primitive = getattr(type_, "from_primitive", None)
    if from_primitive:
      return from_primitive(value)
