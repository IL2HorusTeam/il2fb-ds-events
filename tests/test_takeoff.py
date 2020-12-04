import datetime
import unittest

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.takeoff import HumanAircraftTookOffEvent
from il2fb.ds.events.definitions.takeoff import HumanAircraftTookOffInfo

from il2fb.ds.events.definitions import registry


class HumanAircraftTookOffEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanAircraftTookOffEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanAircraftTookOffEvent"),
      HumanAircraftTookOffEvent,
    )

  def test_to_primitive(self):
    testee = HumanAircraftTookOffEvent(HumanAircraftTookOffInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'take-off',
      'name': 'HumanAircraftTookOffEvent',
      'verbose_name': 'Human aircraft took-off',
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
    testee = HumanAircraftTookOffEvent(HumanAircraftTookOffInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanAircraftTookOffEvent.from_primitive(testee.to_primitive()),
    )
