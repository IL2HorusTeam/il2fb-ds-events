import unittest

from il2fb.commons.actors import HumanActor

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.connection import ChannelInfo
from il2fb.ds.events.definitions.connection import HumanConnectionStartedInfo
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedInfo
from il2fb.ds.events.definitions.connection import HumanConnectionLostInfo

from il2fb.ds.events.definitions.connection import HumanConnectionEvent
from il2fb.ds.events.definitions.connection import HumanConnectionStartedEvent
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedEvent
from il2fb.ds.events.definitions.connection import HumanConnectionLostEvent

from il2fb.ds.events.definitions import registry


class HumanConnectionEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanConnectionEvent, Event))


class HumanConnectionStartedEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionStartedEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionStartedEvent"),
      HumanConnectionStartedEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionStartedEvent(
      HumanConnectionStartedInfo(
        ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionStartedEvent',
      'verbose_name': 'Human connection with server started',
      'help_text': None,
      'data': {
        'channel_info': {
          'channel_no': 1,
          'address': '127.0.0.1',
          'port': 21000,
        },
      },
    })

  def test_from_primitive(self):
    testee = HumanConnectionStartedEvent(
      HumanConnectionStartedInfo(
        ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionStartedEvent.from_primitive(testee.to_primitive()),
    )


class HumanConnectionEstablishedEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionEstablishedEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionEstablishedEvent"),
      HumanConnectionEstablishedEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionEstablishedEvent(
      HumanConnectionEstablishedInfo(
        channel_info=ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
        actor=HumanActor(
          callsign="TheUser",
        ),
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionEstablishedEvent',
      'verbose_name': 'Human connection with server established',
      'help_text': None,
      'data': {
        'channel_info': {
          'channel_no': 1,
          'address': '127.0.0.1',
          'port': 21000,
        },
        'actor': {
          'callsign': 'TheUser',
        },
      },
    })

  def test_from_primitive(self):
    testee = HumanConnectionEstablishedEvent(
      HumanConnectionEstablishedInfo(
        channel_info=ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
        actor=HumanActor(
          callsign="TheUser",
        ),
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionEstablishedEvent.from_primitive(testee.to_primitive()),
    )


class HumanConnectionLostEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionLostEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionLostEvent"),
      HumanConnectionLostEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        channel_info=ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
        reason="You have been kicked from the server.",
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionLostEvent',
      'verbose_name': 'Human connection with server lost',
      'help_text': None,
      'data': {
        'channel_info': {
          'channel_no': 1,
          'address': '127.0.0.1',
          'port': 21000,
        },
        'reason': "You have been kicked from the server.",
      },
    })

  def test_to_primitive_no_reason(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        channel_info=ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
        reason=None,
      ),
    )
    primitive = testee.to_primitive()
    self.assertIsNone(primitive['data']['reason'])

  def test_from_primitive(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        channel_info=ChannelInfo(
          address="127.0.0.1",
          port=21000,
          channel_no=1,
        ),
        reason="You have been kicked from the server.",
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionLostEvent.from_primitive(testee.to_primitive()),
    )
