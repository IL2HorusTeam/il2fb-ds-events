import datetime
import unittest

from il2fb.commons.actors import HumanActor

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.briefing import HumanReturnedToBriefingEvent
from il2fb.ds.events.definitions.briefing import HumanReturnedToBriefingInfo

from il2fb.ds.events.definitions import registry


class HumanReturnedToBriefingEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanReturnedToBriefingEvent, Event))

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
