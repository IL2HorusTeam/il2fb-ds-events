import dataclasses

from typing import Any
from typing import Container
from typing import Dict
from typing import Optional
from typing import Text

from .typing import SupportsText


@dataclasses.dataclass(frozen=True)
class VerboseDataclassMixin:
  verbose_name: SupportsText = dataclasses.field(init=False)
  help_text:    SupportsText = dataclasses.field(init=False)


class PrimitiveDataclassMixin:

  def to_primitive(self, excludes: Optional[Container] = None) -> Dict[Text, Any]:
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

    if isinstance(value, SupportsText) and not isinstance(value, str):
      return str(value)

    return value

  @classmethod
  def from_primitive(cls, value: Dict[Text, Any]) -> Any:
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
