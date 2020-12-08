import datetime
import unittest

from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import BridgeActor
from il2fb.commons.actors import BuildingActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import MovingUnitActor
from il2fb.commons.actors import MovingUnitMemberActor
from il2fb.commons.actors import ObjectActor
from il2fb.commons.actors import StationaryUnitActor

from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.shootdowns import ShotdownEvent

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownSelfEvent

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownSelfEvent

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByBridgeEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByBridgeInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByBuildingEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByBuildingInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByMovingUnitEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByMovingUnitInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByMovingUnitMemberEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByMovingUnitMemberInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByObjectEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByObjectInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByStationaryUnitEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByStationaryUnitInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByTreeEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByTreeInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByParatrooperEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByParatrooperInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByBridgeEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByBridgeInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByBuildingEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByBuildingInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByMovingUnitEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByMovingUnitInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByMovingUnitMemberEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByMovingUnitMemberInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByObjectEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByObjectInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByStationaryUnitEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByStationaryUnitInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByTreeEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByTreeInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByParatrooperEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByParatrooperInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftAndAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftAndAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftAndHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByAIAircraftAndHumanAircraftInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftAndAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftAndAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import AIAircraftShotdownByHumanAircraftAndHumanAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftAndAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftAndAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByAIAircraftAndHumanAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftAndAIAircraftInfo

from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent
from il2fb.ds.events.definitions.shootdowns import HumanAircraftShotdownByHumanAircraftAndHumanAircraftInfo

from il2fb.ds.events.definitions import registry


class ShootdownEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(ShotdownEvent, Event))


class AIAircraftShotdownEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownEvent"),
      AIAircraftShotdownEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownEvent(AIAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownEvent',
      'verbose_name': 'AI aircraft shot down',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownEvent(AIAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownSelfEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownSelfEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownSelfEvent"),
      AIAircraftShotdownSelfEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownSelfEvent(AIAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownSelfEvent',
      'verbose_name': 'AI aircraft shot down self',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownSelfEvent(AIAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownSelfEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownEvent"),
      HumanAircraftShotdownEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownEvent(HumanAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownEvent',
      'verbose_name': 'Human aircraft shot down',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownEvent(HumanAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownSelfEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownSelfEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownSelfEvent"),
      HumanAircraftShotdownSelfEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownSelfEvent(HumanAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownSelfEvent',
      'verbose_name': 'Human aircraft shot down self',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownSelfEvent(HumanAircraftShotdownInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownSelfEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByAIAircraftEvent"),
      AIAircraftShotdownByAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByAIAircraftEvent(AIAircraftShotdownByAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByAIAircraftEvent',
      'verbose_name': 'AI aircraft shot down by AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByAIAircraftEvent(AIAircraftShotdownByAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByBridgeEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByBridgeEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByBridgeEvent"),
      AIAircraftShotdownByBridgeEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByBridgeEvent(AIAircraftShotdownByBridgeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=BridgeActor(
        id="Bridge159",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByBridgeEvent',
      'verbose_name': 'AI aircraft shot down by bridge',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': 'Bridge159',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByBridgeEvent(AIAircraftShotdownByBridgeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=BridgeActor(
        id="Bridge159",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByBridgeEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByBuildingEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByBuildingEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByBuildingEvent"),
      AIAircraftShotdownByBuildingEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByBuildingEvent(AIAircraftShotdownByBuildingInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=BuildingActor(
        id='194_bld',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByBuildingEvent',
      'verbose_name': 'AI aircraft shot down by building',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': '194_bld',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByBuildingEvent(AIAircraftShotdownByBuildingInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=BuildingActor(
        id='194_bld',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByBuildingEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByHumanAircraftEvent"),
      AIAircraftShotdownByHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftEvent(AIAircraftShotdownByHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByHumanAircraftEvent',
      'verbose_name': 'AI aircraft shot down by human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftEvent(AIAircraftShotdownByHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByMovingUnitEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByMovingUnitEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByMovingUnitEvent"),
      AIAircraftShotdownByMovingUnitEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByMovingUnitEvent(AIAircraftShotdownByMovingUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=MovingUnitActor(
        id="0_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByMovingUnitEvent',
      'verbose_name': 'AI aircraft shot down by moving unit',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': '0_Chief',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByMovingUnitEvent(AIAircraftShotdownByMovingUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=MovingUnitActor(
        id="0_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByMovingUnitEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByMovingUnitMemberEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByMovingUnitMemberEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByMovingUnitMemberEvent"),
      AIAircraftShotdownByMovingUnitMemberEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByMovingUnitMemberEvent(AIAircraftShotdownByMovingUnitMemberInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=MovingUnitMemberActor(
        id="0_Chief",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByMovingUnitMemberEvent',
      'verbose_name': 'AI aircraft shot down by moving unit member',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': '0_Chief',
          'member_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByMovingUnitMemberEvent(AIAircraftShotdownByMovingUnitMemberInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=MovingUnitMemberActor(
        id="0_Chief",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByMovingUnitMemberEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByObjectEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByObjectEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByObjectEvent"),
      AIAircraftShotdownByObjectEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByObjectEvent(AIAircraftShotdownByObjectInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=ObjectActor(
        id='3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByObjectEvent',
      'verbose_name': 'AI aircraft shot down by object',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': '3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByObjectEvent(AIAircraftShotdownByObjectInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=ObjectActor(
        id='3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByObjectEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByStationaryUnitEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByStationaryUnitEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByStationaryUnitEvent"),
      AIAircraftShotdownByStationaryUnitEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByStationaryUnitEvent(AIAircraftShotdownByStationaryUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=StationaryUnitActor(
        id='8165_Static',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByStationaryUnitEvent',
      'verbose_name': 'AI aircraft shot down by stationary unit',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'id': '8165_Static',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByStationaryUnitEvent(AIAircraftShotdownByStationaryUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=StationaryUnitActor(
        id='8165_Static',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByStationaryUnitEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByTreeEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByTreeEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByTreeEvent"),
      AIAircraftShotdownByTreeEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByTreeEvent(AIAircraftShotdownByTreeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByTreeEvent',
      'verbose_name': 'AI aircraft shot down by tree',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByTreeEvent(AIAircraftShotdownByTreeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByTreeEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByParatrooperEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByParatrooperEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByParatrooperEvent"),
      AIAircraftShotdownByParatrooperEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByParatrooperEvent(AIAircraftShotdownByParatrooperInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByParatrooperEvent',
      'verbose_name': 'AI aircraft shot down by paratrooper',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByParatrooperEvent(AIAircraftShotdownByParatrooperInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByParatrooperEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByAIAircraftEvent"),
      HumanAircraftShotdownByAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftEvent(HumanAircraftShotdownByAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByAIAircraftEvent',
      'verbose_name': 'Human aircraft shot down by AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftEvent(HumanAircraftShotdownByAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByBridgeEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByBridgeEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByBridgeEvent"),
      HumanAircraftShotdownByBridgeEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByBridgeEvent(HumanAircraftShotdownByBridgeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=BridgeActor(
        id="Bridge159",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByBridgeEvent',
      'verbose_name': 'Human aircraft shot down by bridge',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': 'Bridge159',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByBridgeEvent(HumanAircraftShotdownByBridgeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=BridgeActor(
        id="Bridge159",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByBridgeEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByBuildingEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByBuildingEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByBuildingEvent"),
      HumanAircraftShotdownByBuildingEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByBuildingEvent(HumanAircraftShotdownByBuildingInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=BuildingActor(
        id='194_bld',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByBuildingEvent',
      'verbose_name': 'Human aircraft shot down by building',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': '194_bld',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByBuildingEvent(HumanAircraftShotdownByBuildingInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=BuildingActor(
        id='194_bld',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByBuildingEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByHumanAircraftEvent"),
      HumanAircraftShotdownByHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftEvent(HumanAircraftShotdownByHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByHumanAircraftEvent',
      'verbose_name': 'Human aircraft shot down by human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'callsign': 'TheUser2',
          'aircraft': 'Bf-109F-4',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftEvent(HumanAircraftShotdownByHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByMovingUnitEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByMovingUnitEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByMovingUnitEvent"),
      HumanAircraftShotdownByMovingUnitEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByMovingUnitEvent(HumanAircraftShotdownByMovingUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=MovingUnitActor(
        id="0_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByMovingUnitEvent',
      'verbose_name': 'Human aircraft shot down by moving unit',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': '0_Chief',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByMovingUnitEvent(HumanAircraftShotdownByMovingUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=MovingUnitActor(
        id="0_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByMovingUnitEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByMovingUnitMemberEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByMovingUnitMemberEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByMovingUnitMemberEvent"),
      HumanAircraftShotdownByMovingUnitMemberEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByMovingUnitMemberEvent(HumanAircraftShotdownByMovingUnitMemberInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=MovingUnitMemberActor(
        id="0_Chief",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByMovingUnitMemberEvent',
      'verbose_name': 'Human aircraft shot down by moving unit member',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': '0_Chief',
          'member_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByMovingUnitMemberEvent(HumanAircraftShotdownByMovingUnitMemberInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=MovingUnitMemberActor(
        id="0_Chief",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByMovingUnitMemberEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByObjectEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByObjectEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByObjectEvent"),
      HumanAircraftShotdownByObjectEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByObjectEvent(HumanAircraftShotdownByObjectInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=ObjectActor(
        id='3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByObjectEvent',
      'verbose_name': 'Human aircraft shot down by object',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': '3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByObjectEvent(HumanAircraftShotdownByObjectInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=ObjectActor(
        id='3do/Buildings/Airdrome/BarrelBlock1/mono.sim',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByObjectEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByStationaryUnitEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByStationaryUnitEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByStationaryUnitEvent"),
      HumanAircraftShotdownByStationaryUnitEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByStationaryUnitEvent(HumanAircraftShotdownByStationaryUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=StationaryUnitActor(
        id='8165_Static',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByStationaryUnitEvent',
      'verbose_name': 'Human aircraft shot down by stationary unit',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'id': '8165_Static',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByStationaryUnitEvent(HumanAircraftShotdownByStationaryUnitInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=StationaryUnitActor(
        id='8165_Static',
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByStationaryUnitEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByTreeEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByTreeEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByTreeEvent"),
      HumanAircraftShotdownByTreeEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByTreeEvent(HumanAircraftShotdownByTreeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByTreeEvent',
      'verbose_name': 'Human aircraft shot down by tree',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByTreeEvent(HumanAircraftShotdownByTreeInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByTreeEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByParatrooperEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByParatrooperEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByParatrooperEvent"),
      HumanAircraftShotdownByParatrooperEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByParatrooperEvent(HumanAircraftShotdownByParatrooperInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByParatrooperEvent',
      'verbose_name': 'Human aircraft shot down by paratrooper',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByParatrooperEvent(HumanAircraftShotdownByParatrooperInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByParatrooperEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByAIAircraftAndAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByAIAircraftAndAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByAIAircraftAndAIAircraftEvent"),
      AIAircraftShotdownByAIAircraftAndAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByAIAircraftAndAIAircraftEvent(AIAircraftShotdownByAIAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=1,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByAIAircraftAndAIAircraftEvent',
      'verbose_name': 'AI aircraft shot down by AI aircraft and AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'assistant': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 1,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByAIAircraftAndAIAircraftEvent(AIAircraftShotdownByAIAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=1,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByAIAircraftAndAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByAIAircraftAndHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByAIAircraftAndHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByAIAircraftAndHumanAircraftEvent"),
      AIAircraftShotdownByAIAircraftAndHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByAIAircraftAndHumanAircraftEvent(AIAircraftShotdownByAIAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByAIAircraftAndHumanAircraftEvent',
      'verbose_name': 'AI aircraft shot down by AI aircraft and human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'assistant': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByAIAircraftAndHumanAircraftEvent(AIAircraftShotdownByAIAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByAIAircraftAndHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByHumanAircraftAndAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByHumanAircraftAndAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByHumanAircraftAndAIAircraftEvent"),
      AIAircraftShotdownByHumanAircraftAndAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftAndAIAircraftEvent(AIAircraftShotdownByHumanAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByHumanAircraftAndAIAircraftEvent',
      'verbose_name': 'AI aircraft shot down by human aircraft and AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'assistant': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftAndAIAircraftEvent(AIAircraftShotdownByHumanAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByHumanAircraftAndAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftShotdownByHumanAircraftAndHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent"),
      AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent(AIAircraftShotdownByHumanAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent',
      'verbose_name': 'AI aircraft shot down by human aircraft and human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'attacker': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'assistant': {
          'callsign': 'TheUser2',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent(AIAircraftShotdownByHumanAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftShotdownByHumanAircraftAndHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByAIAircraftAndAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByAIAircraftAndAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByAIAircraftAndAIAircraftEvent"),
      HumanAircraftShotdownByAIAircraftAndAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftAndAIAircraftEvent(HumanAircraftShotdownByAIAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=1,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByAIAircraftAndAIAircraftEvent',
      'verbose_name': 'Human aircraft shot down by AI aircraft and AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'assistant': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 1,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftAndAIAircraftEvent(HumanAircraftShotdownByAIAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=1,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByAIAircraftAndAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByAIAircraftAndHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent"),
      HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent(HumanAircraftShotdownByAIAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent',
      'verbose_name': 'Human aircraft shot down by AI aircraft and human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'assistant': {
          'callsign': 'TheUser2',
          'aircraft': 'Bf-109F-4',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent(HumanAircraftShotdownByAIAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByAIAircraftAndHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByHumanAircraftAndAIAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent"),
      HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent(HumanAircraftShotdownByHumanAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent',
      'verbose_name': 'Human aircraft shot down by human aircraft and AI aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'callsign': 'TheUser2',
          'aircraft': 'Bf-109F-4',
        },
        'assistant': {
          'regiment_id': 'g01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent(HumanAircraftShotdownByHumanAircraftAndAIAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      assistant=AIAircraftActor(
        regiment_id="g01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByHumanAircraftAndAIAircraftEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftShotdownByHumanAircraftAndHumanAircraftEventTestCase(unittest.TestCase):

  def test_derives_from_ShootdownEvent(self):
    self.assertTrue(issubclass(HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent, ShotdownEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent"),
      HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent(HumanAircraftShotdownByHumanAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser3",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'shotdown',
      'name': 'HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent',
      'verbose_name': 'Human aircraft shot down by human aircraft and human aircraft',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'attacker': {
          'callsign': 'TheUser2',
          'aircraft': 'Bf-109F-4',
        },
        'assistant': {
          'callsign': 'TheUser3',
          'aircraft': 'Bf-109F-4',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent(HumanAircraftShotdownByHumanAircraftAndHumanAircraftInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      target=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      attacker=HumanAircraftActor(
        callsign="TheUser2",
        aircraft="Bf-109F-4",
      ),
      assistant=HumanAircraftActor(
        callsign="TheUser3",
        aircraft="Bf-109F-4",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftShotdownByHumanAircraftAndHumanAircraftEvent.from_primitive(testee.to_primitive()),
    )
