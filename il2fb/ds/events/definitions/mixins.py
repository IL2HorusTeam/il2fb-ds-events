import datetime

from dataclasses import dataclass

from il2fb.commons.spatial import Point3D


@dataclass(frozen=True)
class TimestampMixin:
  timestamp: datetime.datetime


@dataclass(frozen=True)
class PositionMixin:
  pos: Point3D
