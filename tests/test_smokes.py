import datetime
import unittest

from il2fb.commons.actors import HumanAircraftActor
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.smokes import HumanToggledWingtipSmokesEvent
from il2fb.ds.events.definitions.smokes import HumanToggledWingtipSmokesInfo

from il2fb.ds.events.definitions import registry


class HumanToggledWingtipSmokesEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanToggledWingtipSmokesEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanToggledWingtipSmokesEvent"),
      HumanToggledWingtipSmokesEvent,
    )

  def test_to_primitive(self):
    testee = HumanToggledWingtipSmokesEvent(HumanToggledWingtipSmokesInfo(
      timestamp=datetime.time(23, 45, 59),
      state=True,
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      coord=Point3D(71903.14, 41619.023, 5399.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'smokes',
      'name': 'HumanToggledWingtipSmokesEvent',
      'verbose_name': 'Human toggled wingtip smokes',
      'help_text': None,
      'data': {
        'timestamp': "23:45:59",
        'state': True,
        'actor': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
        },
        'coord': {
          'x': 71903.14,
          'y': 41619.023,
          'z': 5399.754,
        },
      },
    })

  def test_from_primitive(self):
    testee = HumanToggledWingtipSmokesEvent(HumanToggledWingtipSmokesInfo(
      timestamp=datetime.time(23, 45, 59),
      state=True,
      actor=HumanAircraftActor(
        callsign="TheUser",
        aircraft="P-39D2",
      ),
      coord=Point3D(71903.14, 41619.023, 5399.754),
    ))
    self.assertEqual(
      testee,
      HumanToggledWingtipSmokesEvent.from_primitive(testee.to_primitive()),
    )
