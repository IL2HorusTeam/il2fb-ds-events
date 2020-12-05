import datetime
import unittest

from il2fb.commons.actors import AIAircraftActor
from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.actors import UnknownActor

from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.spawning import SpawningEvent

from il2fb.ds.events.definitions.spawning import HumanAircraftSpawnedEvent
from il2fb.ds.events.definitions.spawning import HumanAircraftSpawnedInfo

from il2fb.ds.events.definitions.spawning import HumanAircraftDespawnedEvent
from il2fb.ds.events.definitions.spawning import HumanAircraftDespawnedInfo

from il2fb.ds.events.definitions.spawning import AIAircraftDespawnedEvent
from il2fb.ds.events.definitions.spawning import AIAircraftDespawnedInfo

from il2fb.ds.events.definitions.spawning import UnknownActorDespawnedEvent
from il2fb.ds.events.definitions.spawning import UnknownActorDespawnedInfo

from il2fb.ds.events.definitions import registry


class SpawningEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(SpawningEvent, Event))


class HumanAircraftSpawnedEventTestCase(unittest.TestCase):

  def test_derives_from_SpawningEvent(self):
    self.assertTrue(issubclass(HumanAircraftSpawnedEvent, SpawningEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftSpawnedEvent"),
      HumanAircraftSpawnedEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftSpawnedEvent(HumanAircraftSpawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      weapons="2xfab500",
      fuel=100,
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'spawning',
      'name': 'HumanAircraftSpawnedEvent',
      'verbose_name': 'Human aircraft spawned',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'weapons': '2xfab500',
        'fuel': 100,
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftSpawnedEvent(HumanAircraftSpawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      weapons="2xfab500",
      fuel=100,
    ))
    self.assertEqual(
      testee,
      HumanAircraftSpawnedEvent.from_primitive(testee.to_primitive()),
    )


class HumanAircraftDespawnedEventTestCase(unittest.TestCase):

  def test_derives_from_SpawningEvent(self):
    self.assertTrue(issubclass(HumanAircraftDespawnedEvent, SpawningEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftDespawnedEvent"),
      HumanAircraftDespawnedEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftDespawnedEvent(HumanAircraftDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'spawning',
      'name': 'HumanAircraftDespawnedEvent',
      'verbose_name': 'Human aircraft despawned',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 82.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanAircraftDespawnedEvent(HumanAircraftDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftDespawnedEvent.from_primitive(testee.to_primitive()),
    )


class AIAircraftDespawnedEventTestCase(unittest.TestCase):

  def test_derives_from_SpawningEvent(self):
    self.assertTrue(issubclass(AIAircraftDespawnedEvent, SpawningEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("AIAircraftDespawnedEvent"),
      AIAircraftDespawnedEvent,
    )

  def test_to_primitive(self):
    testee = AIAircraftDespawnedEvent(AIAircraftDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'spawning',
      'name': 'AIAircraftDespawnedEvent',
      'verbose_name': 'AI aircraft despawned',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'regiment_id': 'r01',
          'squadron_id': 0,
          'flight_id': 0,
          'flight_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 82.754},
      },
    })

  def test_from_primitive(self):
    testee = AIAircraftDespawnedEvent(AIAircraftDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=AIAircraftActor(
        regiment_id="r01",
        squadron_id=0,
        flight_id=0,
        flight_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(
      testee,
      AIAircraftDespawnedEvent.from_primitive(testee.to_primitive()),
    )


class UnknownActorDespawnedEventTestCase(unittest.TestCase):

  def test_derives_from_SpawningEvent(self):
    self.assertTrue(issubclass(UnknownActorDespawnedEvent, SpawningEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("UnknownActorDespawnedEvent"),
      UnknownActorDespawnedEvent,
    )

  def test_to_primitive(self):
    testee = UnknownActorDespawnedEvent(UnknownActorDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=UnknownActor(
        id="foo",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'spawning',
      'name': 'UnknownActorDespawnedEvent',
      'verbose_name': 'Unknown actor despawned',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'id': 'foo',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 82.754},
      },
    })

  def test_from_primitive(self):
    testee = UnknownActorDespawnedEvent(UnknownActorDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=UnknownActor(
        id="foo",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(
      testee,
      UnknownActorDespawnedEvent.from_primitive(testee.to_primitive()),
    )
