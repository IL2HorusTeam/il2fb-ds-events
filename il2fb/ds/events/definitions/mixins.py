import datetime

from dataclasses import dataclass

from il2fb.commons.spatial import Point3D


@dataclass(frozen=True)
class DatetimeMixin:
  timestamp: datetime.datetime


@dataclass(frozen=True)
class TimeMixin:
  timestamp: datetime.time


@dataclass(frozen=True)
class CoordinatesMixin:
  coord: Point3D
