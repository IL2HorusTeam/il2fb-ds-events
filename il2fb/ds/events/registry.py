from typing import Type

from .exceptions import EventRegistryLookupError
from .typing import Event
from .utils import export


_event_classes_registry = dict()


@export
def register(cls: Type[Event]) -> None:
  """
  Decorator for final event classes.

  """
  _event_classes_registry[cls.__name__] = cls
  return cls


@export
def get_class_by_name(name: str) -> Type[Event]:
  """
  Get event class by event's name.

  :raises EventRegistryLookupError: if event with a given name is not registered

  """
  return _event_classes_registry[name]
