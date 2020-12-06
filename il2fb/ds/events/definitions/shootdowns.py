from dataclasses import dataclass

from il2fb.commons.actors import Actor

from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import BridgeActor
from il2fb.commons.actors import BuildingActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import MovingUnitActor
from il2fb.commons.actors import MovingUnitMemberActor
from il2fb.commons.actors import ObjectActor
from il2fb.commons.actors import StationaryUnitActor
from il2fb.commons.actors import UnknownActor

from il2fb.commons.structures import PrimitiveDataclassMixin

from .base import Event

from .mixins import TimestampMixin
from .mixins import PositionMixin

from .registry import register

from ._utils import export
from ._translations import gettext_lazy as _


@export
@dataclass(frozen=True)
class ShotdownInfo(TimestampMixin, PositionMixin, PrimitiveDataclassMixin):
  __slots__ = ["timestamp", "pos", "target", ]

  target: Actor


@export
@dataclass(frozen=True)
class ShotdownBySingleInfo(ShotdownInfo):
  __slots__ = ShotdownInfo.__slots__ + ["attacker", ]

  attacker: Actor


@export
@dataclass(frozen=True)
class ShotdownByPairInfo(ShotdownBySingleInfo):
  __slots__ = ShotdownBySingleInfo.__slots__ + ["assistant", ]

  assistant: Actor


@export
@dataclass(frozen=True)
class ShotdownEvent(Event):
  category = "shotdown"


@export
@dataclass(frozen=True)
class AIAircraftShotdownInfo(ShotdownInfo):
  target: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down")
  data: AIAircraftShotdownInfo


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownSelfEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down self")
  data: AIAircraftShotdownInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownInfo(ShotdownInfo):
  target: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down")
  data: HumanAircraftShotdownInfo


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownSelfEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down self")
  data: HumanAircraftShotdownInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by AI aircraft")
  data: AIAircraftShotdownByAIAircraftInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByBridgeInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: BridgeActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByBridgeEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by bridge")
  data: AIAircraftShotdownByBridgeInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByBuildingInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: BuildingActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByBuildingEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by building")
  data: AIAircraftShotdownByBuildingInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by human aircraft")
  data: AIAircraftShotdownByHumanAircraftInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByMovingUnitInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: MovingUnitActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByMovingUnitEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by moving unit")
  data: AIAircraftShotdownByMovingUnitInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByMovingUnitMemberInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: MovingUnitMemberActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByMovingUnitMemberEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by moving unit member")
  data: AIAircraftShotdownByMovingUnitMemberInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByObjectInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: ObjectActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByObjectEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by object")
  data: AIAircraftShotdownByObjectInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByStationaryUnitInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: StationaryUnitActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByStationaryUnitEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by stationary unit")
  data: AIAircraftShotdownByStationaryUnitInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByTreeInfo(ShotdownInfo):
  target: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByTreeEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by tree")
  data: AIAircraftShotdownByTreeInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByParatrooperInfo(ShotdownInfo):
  target: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByParatrooperEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by paratrooper")
  data: AIAircraftShotdownByParatrooperInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByUnknownActorInfo(ShotdownBySingleInfo):
  target:   AIAircraftActor
  attacker: UnknownActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByUnknownActorEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by unknown actor")
  data: AIAircraftShotdownByUnknownActorInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by AI aircraft")
  data: HumanAircraftShotdownByAIAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByBridgeInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: BridgeActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByBridgeEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by bridge")
  data: HumanAircraftShotdownByBridgeInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByBuildingInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: BuildingActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByBuildingEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by building")
  data: HumanAircraftShotdownByBuildingInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by human aircraft")
  data: HumanAircraftShotdownByHumanAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByMovingUnitInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: MovingUnitActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByMovingUnitEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by moving unit")
  data: HumanAircraftShotdownByMovingUnitInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByMovingUnitMemberInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: MovingUnitMemberActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByMovingUnitMemberEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by moving unit member")
  data: HumanAircraftShotdownByMovingUnitMemberInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByObjectInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: ObjectActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByObjectEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by object")
  data: HumanAircraftShotdownByObjectInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByStationaryUnitInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: StationaryUnitActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByStationaryUnitEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by stationary unit")
  data: HumanAircraftShotdownByStationaryUnitInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByTreeInfo(ShotdownInfo):
  target: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByTreeEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by tree")
  data: HumanAircraftShotdownByTreeInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByParatrooperInfo(ShotdownInfo):
  target: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByParatrooperEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by paratrooper")
  data: HumanAircraftShotdownByParatrooperInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByUnknownActorInfo(ShotdownBySingleInfo):
  target:   HumanAircraftActor
  attacker: UnknownActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByUnknownActorEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by unknown actor")
  data: HumanAircraftShotdownByUnknownActorInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftAndAIAircraftInfo(ShotdownByPairInfo):
  target:    AIAircraftActor
  attacker:  AIAircraftActor
  assistant: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftAndAIAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by AI aircraft and AI aircraft")
  data: AIAircraftShotdownByAIAircraftAndAIAircraftInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftAndHumanAircraftInfo(ShotdownByPairInfo):
  target:    AIAircraftActor
  attacker:  AIAircraftActor
  assistant: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByAIAircraftAndHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by AI aircraft and human aircraft")
  data: AIAircraftShotdownByAIAircraftAndHumanAircraftInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftAndAIAircraftInfo(ShotdownByPairInfo):
  target:    AIAircraftActor
  attacker:  HumanAircraftActor
  assistant: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftAndAIAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by human aircraft and AI aircraft")
  data: AIAircraftShotdownByHumanAircraftAndAIAircraftInfo


@export
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftAndHumanAircraftInfo(ShotdownByPairInfo):
  target:    AIAircraftActor
  attacker:  HumanAircraftActor
  assistant: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("AI aircraft shot down by human aircraft and human aircraft")
  data: AIAircraftShotdownByHumanAircraftAndHumanAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftAndAIAircraftInfo(ShotdownByPairInfo):
  target:    HumanAircraftActor
  attacker:  AIAircraftActor
  assistant: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftAndAIAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by AI aircraft and AI aircraft")
  data: HumanAircraftShotdownByAIAircraftAndAIAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftAndHumanAircraftInfo(ShotdownByPairInfo):
  target:    HumanAircraftActor
  attacker:  AIAircraftActor
  assistant: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by AI aircraft and human aircraft")
  data: HumanAircraftShotdownByAIAircraftAndHumanAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftAndAIAircraftInfo(ShotdownByPairInfo):
  target:    HumanAircraftActor
  attacker:  HumanAircraftActor
  assistant: AIAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by human aircraft and AI aircraft")
  data: HumanAircraftShotdownByHumanAircraftAndAIAircraftInfo


@export
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftAndHumanAircraftInfo(ShotdownByPairInfo):
  target:    HumanAircraftActor
  attacker:  HumanAircraftActor
  assistant: HumanAircraftActor


@export
@register
@dataclass(frozen=True)
class HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent(ShotdownEvent):
  verbose_name = _("Human aircraft shot down by human aircraft and human aircraft")
  data: HumanAircraftShotdownByHumanAircraftAndHumanAircraftInfo
