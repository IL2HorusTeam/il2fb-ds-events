import datetime

from dataclasses import dataclass


@dataclass(frozen=True)
class DatetimeMixin:
  timestamp: datetime.datetime


@dataclass(frozen=True)
class TimeMixin:
  timestamp: datetime.time
