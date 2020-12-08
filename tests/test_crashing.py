import datetime
import unittest

from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import MovingUnitActor
from il2fb.commons.actors import MovingUnitMemberActor
from il2fb.commons.actors import StationaryUnitActor

from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.crashing import CrashingEvent

from il2fb.ds.events.definitions.crashing import AIAircraftCrashedEvent
from il2fb.ds.events.definitions.crashing import AIAircraftCrashedInfo

from il2fb.ds.events.definitions.crashing import HumanAircraftCrashedEvent
from il2fb.ds.events.definitions.crashing import HumanAircraftCrashedInfo

from il2fb.ds.events.definitions.crashing import MovingUnitCrashedEvent
from il2fb.ds.events.definitions.crashing import MovingUnitCrashedInfo

from il2fb.ds.events.definitions.crashing import MovingUnitMemberCrashedEvent
from il2fb.ds.events.definitions.crashing import MovingUnitMemberCrashedInfo

from il2fb.ds.events.definitions.crashing import StationaryUnitCrashedEvent
from il2fb.ds.events.definitions.crashing import StationaryUnitCrashedInfo

from il2fb.ds.events.definitions import registry


class CrashingEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(CrashingEvent, Event))


class HumanAircraftCrashedEventTestCase(unittest.TestCase):

  def test_derives_from_CrashingEvent(self):
    self.assertTrue(issubclass(HumanAircraftCrashedEvent, CrashingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftCrashedEvent"),
      HumanAircraftCrashedEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftCrashedEvent(HumanAircraftCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'crash',
      'name': 'HumanAircraftCrashedEvent',
      'verbose_name': 'Human aircraft crashed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftCrashedEvent(HumanAircraftCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftCrashedEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftCrashedEventTestCase(unittest.TestCase):

  def test_derives_from_CrashingEvent(self):
    self.assertTrue(issubclass(AIAircraftCrashedEvent, CrashingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftCrashedEvent"),
      AIAircraftCrashedEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftCrashedEvent(AIAircraftCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'crash',
      'name': 'AIAircraftCrashedEvent',
      'verbose_name': 'AI aircraft crashed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftCrashedEvent(AIAircraftCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftCrashedEvent.from_primitive(testee.to_primitive()),
    )


class MovingUnitCrashedEventTestCase(unittest.TestCase):

  def test_derives_from_CrashingEvent(self):
    self.assertTrue(issubclass(MovingUnitCrashedEvent, CrashingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("MovingUnitCrashedEvent"),
      MovingUnitCrashedEvent,
    )

  def test_to_primitive(self):
    testee = MovingUnitCrashedEvent(MovingUnitCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=MovingUnitActor(
        id="12004_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'crash',
      'name': 'MovingUnitCrashedEvent',
      'verbose_name': 'Moving unit crashed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'id': '12004_Chief',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = MovingUnitCrashedEvent(MovingUnitCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=MovingUnitActor(
        id="12004_Chief",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      MovingUnitCrashedEvent.from_primitive(testee.to_primitive()),
    )


class MovingUnitMemberCrashedEventTestCase(unittest.TestCase):

  def test_derives_from_CrashingEvent(self):
    self.assertTrue(issubclass(MovingUnitMemberCrashedEvent, CrashingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("MovingUnitMemberCrashedEvent"),
      MovingUnitMemberCrashedEvent,
    )

  def test_to_primitive(self):
    testee = MovingUnitMemberCrashedEvent(MovingUnitMemberCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=MovingUnitMemberActor(
        id="12004_Chief",
        member_index=10,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'crash',
      'name': 'MovingUnitMemberCrashedEvent',
      'verbose_name': 'Moving unit member crashed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'id': '12004_Chief',
          'member_index': 10,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = MovingUnitMemberCrashedEvent(MovingUnitMemberCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=MovingUnitMemberActor(
        id="12004_Chief",
        member_index=10,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      MovingUnitMemberCrashedEvent.from_primitive(testee.to_primitive()),
    )


class StationaryUnitCrashedEventTestCase(unittest.TestCase):

  def test_derives_from_CrashingEvent(self):
    self.assertTrue(issubclass(StationaryUnitCrashedEvent, CrashingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("StationaryUnitCrashedEvent"),
      StationaryUnitCrashedEvent,
    )

  def test_to_primitive(self):
    testee = StationaryUnitCrashedEvent(StationaryUnitCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=StationaryUnitActor(
        id="7037_Static",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'crash',
      'name': 'StationaryUnitCrashedEvent',
      'verbose_name': 'Stationary unit crashed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'id': '7037_Static',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = StationaryUnitCrashedEvent(StationaryUnitCrashedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=StationaryUnitActor(
        id="7037_Static",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      StationaryUnitCrashedEvent.from_primitive(testee.to_primitive()),
    )
