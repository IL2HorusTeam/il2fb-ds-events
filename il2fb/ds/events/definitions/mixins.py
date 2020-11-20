import datetime

from dataclasses import dataclass


@dataclass(frozen=True)
class TimeMixin:
  time: datetime.time
