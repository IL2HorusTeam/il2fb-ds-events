import datetime
import unittest

from il2fb.commons.actors import HumanActor

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.recording import HumanToggledRecordingEvent
from il2fb.ds.events.definitions.recording import HumanToggledRecordingInfo

from il2fb.ds.events.definitions import registry


class HumanToggledRecordingEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanToggledRecordingEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanToggledRecordingEvent"),
      HumanToggledRecordingEvent,
    )

  def test_to_primitive(self):
    testee = HumanToggledRecordingEvent(HumanToggledRecordingInfo(
      timestamp=datetime.time(23, 45, 59),
      state=True,
      actor=HumanActor(
        callsign="TheUser",
      ),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'recording',
      'name': 'HumanToggledRecordingEvent',
      'verbose_name': 'Human toggled track recording',
      'help_text': None,
      'data': {
        'timestamp': "23:45:59",
        'state': True,
        'actor': {
          'callsign': 'TheUser',
        },
      },
    })

  def test_from_primitive(self):
    testee = HumanToggledRecordingEvent(HumanToggledRecordingInfo(
      timestamp=datetime.time(23, 45, 59),
      state=True,
      actor=HumanActor(
        callsign="TheUser",
      ),
    ))
    self.assertEqual(
      testee,
      HumanToggledRecordingEvent.from_primitive(testee.to_primitive()),
    )
