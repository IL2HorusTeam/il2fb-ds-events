from typing import Type

from .base import Event
from .exceptions import EventRegistryLookupError

from ._utils import export


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
  try:
    return _event_classes_registry[name]
  except KeyError as e:
    raise EventRegistryLookupError from e
