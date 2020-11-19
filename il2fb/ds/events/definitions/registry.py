from typing import Type

from .base import Event
from .exceptions import EventRegistryLookupError

from ._utils import export


@export
class EventsRegistry:

  def __init__(self):
    self._data = dict()

  def register(self, cls: Type[Event]) -> None:
    """
    Register event class.

    Can be used as decorator.

    """
    self._data[cls.__name__] = cls
    return cls

  def get_class_by_name(self, name: str) -> Type[Event]:
    """
    Get event class by event's name.

    :raises EventRegistryLookupError: if event with a given name is not registered

    """
    try:
      return self._data[name]
    except KeyError as e:
      raise EventRegistryLookupError from e


# default registry
registry = EventsRegistry()

register = registry.register
get_class_by_name = registry.get_class_by_name
