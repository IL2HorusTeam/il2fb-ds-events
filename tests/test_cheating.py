import unittest

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.cheating import CheatingInfo
from il2fb.ds.events.definitions.cheating import CheatingDetectedEvent

from il2fb.ds.events.definitions import registry


class CheatingDetectedEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(CheatingDetectedEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("CheatingDetectedEvent"),
      CheatingDetectedEvent,
    )

  def test_to_primitive(self):
    testee = CheatingDetectedEvent(CheatingInfo(
      channel_no=207,
      cheat_code=8,
      cheat_details="Cheat-Engine",
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'cheating',
      'name': 'CheatingDetectedEvent',
      'verbose_name': 'Cheating detected',
      'help_text': None,
      'data': {
        'channel_no': 207,
        'cheat_code': 8,
        'cheat_details': 'Cheat-Engine',
      },
    })

  def test_from_primitive(self):
    testee = CheatingDetectedEvent(CheatingInfo(
      channel_no=207,
      cheat_code=8,
      cheat_details="Cheat-Engine",
    ))
    self.assertEqual(
      testee,
      CheatingDetectedEvent.from_primitive(testee.to_primitive()),
    )
