import datetime
import unittest

from il2fb.commons.targets import TARGET_STATES

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.targets import TargetStateChangedInfo
from il2fb.ds.events.definitions.targets import TargetStateChangedEvent

from il2fb.ds.events.definitions import registry


class MissionStatusEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(TargetStateChangedEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("TargetStateChangedEvent"),
      TargetStateChangedEvent,
    )

  def test_to_primitive(self):
    testee = TargetStateChangedEvent(TargetStateChangedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      index=3,
      state=TARGET_STATES.COMPLETE,
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'target',
      'name': 'TargetStateChangedEvent',
      'verbose_name': 'Target state changed',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'index': 3,
        'state': 'COMPLETE',
      },
    })

  def test_from_primitive(self):
    testee = TargetStateChangedEvent(TargetStateChangedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      index=3,
      state=TARGET_STATES.COMPLETE,
    ))
    self.assertEqual(
      testee,
      TargetStateChangedEvent.from_primitive(testee.to_primitive()),
    )
