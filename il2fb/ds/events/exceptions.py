from .utils import export


@export
class EventException(Exception):
  """Base class for all exceptions specific to this package."""


@export
class EventRegistryError(EventException):
  pass


@export
class EventRegistryLookupError(LookupError, EventRegistryError):
  pass
