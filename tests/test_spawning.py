import datetime
import unittest

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.spawning import HumanSpawnedEvent
from il2fb.ds.events.definitions.spawning import HumanSpawnedInfo

from il2fb.ds.events.definitions.spawning import HumanDespawnedEvent
from il2fb.ds.events.definitions.spawning import HumanDespawnedInfo

from il2fb.ds.events.definitions import registry


class HumanSpawnedEventTestCase(unittest.TestCase):
  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanSpawnedEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanSpawnedEvent"),
      HumanSpawnedEvent,
    )

  def test_to_primitive(self):
    testee = HumanSpawnedEvent(HumanSpawnedInfo(
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
      'name': 'HumanSpawnedEvent',
      'verbose_name': 'Human spawned',
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
    testee = HumanSpawnedEvent(HumanSpawnedInfo(
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
      HumanSpawnedEvent.from_primitive(testee.to_primitive()),
    )


class HumanDespawnedEventTestCase(unittest.TestCase):
  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanDespawnedEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanDespawnedEvent"),
      HumanDespawnedEvent,
    )

  def test_to_primitive(self):
    testee = HumanDespawnedEvent(HumanDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'spawning',
      'name': 'HumanDespawnedEvent',
      'verbose_name': 'Human despawned',
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
    testee = HumanDespawnedEvent(HumanDespawnedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 82.754),
    ))
    self.assertEqual(
      testee,
      HumanDespawnedEvent.from_primitive(testee.to_primitive()),
    )
