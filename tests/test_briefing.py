import datetime
import unittest

from il2fb.commons.actors import HumanActor
from il2fb.commons.belligerents import BELLIGERENTS
from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.briefing import BriefingEvent
from il2fb.ds.events.definitions.briefing import HumanReturnedToBriefingEvent
from il2fb.ds.events.definitions.briefing import HumanSelectedAirfieldEvent

from il2fb.ds.events.definitions.briefing import HumanReturnedToBriefingInfo
from il2fb.ds.events.definitions.briefing import HumanSelectedAirfieldInfo

from il2fb.ds.events.definitions import registry


class BriefingEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(BriefingEvent, Event))


class HumanReturnedToBriefingEventTestCase(unittest.TestCase):

  def test_derives_from_BriefingEvent(self):
    self.assertTrue(issubclass(HumanReturnedToBriefingEvent, BriefingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanReturnedToBriefingEvent"),
      HumanReturnedToBriefingEvent,
    )

  def test_to_primitive(self):
    testee = HumanReturnedToBriefingEvent(HumanReturnedToBriefingInfo(
      timestamp=datetime.time(23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'briefing',
      'name': 'HumanReturnedToBriefingEvent',
      'verbose_name': 'Human returned to briefing',
      'help_text': None,
      'data': {
        'timestamp': "23:45:59",
        'actor': {
          'callsign': 'TheUser',
        },
      },
    })

  def test_from_primitive(self):
    testee = HumanReturnedToBriefingEvent(HumanReturnedToBriefingInfo(
      timestamp=datetime.time(23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
    ))
    self.assertEqual(
      testee,
      HumanReturnedToBriefingEvent.from_primitive(testee.to_primitive()),
    )


class HumanSelectedAirfieldEventTestCase(unittest.TestCase):

  def test_derives_from_BriefingEvent(self):
    self.assertTrue(issubclass(HumanSelectedAirfieldEvent, BriefingEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanSelectedAirfieldEvent"),
      HumanSelectedAirfieldEvent,
    )

  def test_to_primitive(self):
    testee = HumanSelectedAirfieldEvent(HumanSelectedAirfieldInfo(
      timestamp=datetime.time(23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
      coord=Point3D(71903.14, 41619.023, 5399.754),
      belligerent=BELLIGERENTS.RED,
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'briefing',
      'name': 'HumanSelectedAirfieldEvent',
      'verbose_name': 'Human selected airfield',
      'help_text': None,
      'data': {
        'timestamp': "23:45:59",
        'actor': {
          'callsign': 'TheUser',
        },
        'coord': {
          'x': 71903.14,
          'y': 41619.023,
          'z': 5399.754,
        },
        'belligerent': 'RED',
      },
    })

  def test_from_primitive(self):
    testee = HumanSelectedAirfieldEvent(HumanSelectedAirfieldInfo(
      timestamp=datetime.time(23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
      coord=Point3D(71903.14, 41619.023, 5399.754),
      belligerent=BELLIGERENTS.RED,
    ))
    self.assertEqual(
      testee,
      HumanSelectedAirfieldEvent.from_primitive(testee.to_primitive()),
    )
