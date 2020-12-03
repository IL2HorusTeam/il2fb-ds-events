import datetime
import unittest

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.lights import HumanToggledLandingLightsEvent
from il2fb.ds.events.definitions.lights import HumanToggledLandingLightsInfo

from il2fb.ds.events.definitions import registry


class HumanToggledLandingLightsEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanToggledLandingLightsEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanToggledLandingLightsEvent"),
      HumanToggledLandingLightsEvent,
    )

  def test_to_primitive(self):
    testee = HumanToggledLandingLightsEvent(HumanToggledLandingLightsInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      state=True,
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 5399.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'lights',
      'name': 'HumanToggledLandingLightsEvent',
      'verbose_name': 'Human toggled landing lights',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'state': True,
        'actor': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 5399.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanToggledLandingLightsEvent(HumanToggledLandingLightsInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      state=True,
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      pos=Point3D(71903.14, 41619.023, 5399.754),
    ))
    self.assertEqual(
      testee,
      HumanToggledLandingLightsEvent.from_primitive(testee.to_primitive()),
    )
