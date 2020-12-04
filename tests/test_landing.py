import datetime
import unittest

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.landing import LandingEvent

from il2fb.ds.events.definitions.landing import HumanAircraftLandedEvent
from il2fb.ds.events.definitions.landing import HumanAircraftLandedInfo

from il2fb.ds.events.definitions import registry


class LandingEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(LandingEvent, Event))


class HumanAircraftLandedEventTestCase(unittest.TestCase):

  def test_derives_from_LandingEvent(self):
    self.assertTrue(issubclass(HumanAircraftLandedEvent, LandingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftLandedEvent"),
      HumanAircraftLandedEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftLandedEvent(HumanAircraftLandedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'landing',
      'name': 'HumanAircraftLandedEvent',
      'verbose_name': 'Human aircraft landed',
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
    testee = HumanAircraftLandedEvent(HumanAircraftLandedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftLandedEvent.from_primitive(testee.to_primitive()),
    )
