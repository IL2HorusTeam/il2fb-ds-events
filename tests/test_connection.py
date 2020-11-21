import datetime
import unittest

from il2fb.commons.actors import HumanActor

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.connection import ConnectionAddress

from il2fb.ds.events.definitions.connection import HumanConnectionStartedInfo
from il2fb.ds.events.definitions.connection import HumanConnectionFailedInfo
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedInfo
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedLightInfo
from il2fb.ds.events.definitions.connection import HumanConnectionLostInfo
from il2fb.ds.events.definitions.connection import HumanConnectionLostLightInfo

from il2fb.ds.events.definitions.connection import HumanConnectionEvent
from il2fb.ds.events.definitions.connection import HumanConnectionStartedEvent
from il2fb.ds.events.definitions.connection import HumanConnectionFailedEvent
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedEvent
from il2fb.ds.events.definitions.connection import HumanConnectionEstablishedLightEvent
from il2fb.ds.events.definitions.connection import HumanConnectionLostEvent
from il2fb.ds.events.definitions.connection import HumanConnectionLostLightEvent

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
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionStartedEvent',
      'verbose_name': 'Human connection with server started',
      'help_text': None,
      'data': {
        'address': {'host': '127.0.0.1', 'port': 21000},
        'channel_no': 1,
      },
    })

  def test_from_primitive(self):
    testee = HumanConnectionStartedEvent(
      HumanConnectionStartedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionStartedEvent.from_primitive(testee.to_primitive()),
    )


class HumanConnectionFailedEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionFailedEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionFailedEvent"),
      HumanConnectionFailedEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionFailedEvent(
      HumanConnectionFailedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        reason="Timeout.",
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionFailedEvent',
      'verbose_name': 'Human connection with server failed',
      'help_text': None,
      'data': {
        'address': {'host': '127.0.0.1', 'port': 21000},
        'reason': "Timeout.",
      },
    })

  def test_to_primitive_no_reason(self):
    testee = HumanConnectionFailedEvent(
      HumanConnectionFailedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        reason=None,
      ),
    )
    primitive = testee.to_primitive()
    self.assertIsNone(primitive['data']['reason'])

  def test_from_primitive(self):
    testee = HumanConnectionFailedEvent(
      HumanConnectionFailedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        reason="Timeout.",
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionFailedEvent.from_primitive(testee.to_primitive()),
    )

  def test_from_primitive_no_reason(self):
    testee = HumanConnectionFailedEvent(
      HumanConnectionFailedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        reason=None,
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionFailedEvent.from_primitive(testee.to_primitive()),
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
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
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
        'address': {'host': '127.0.0.1', 'port': 21000},
        'channel_no': 1,
        'actor': {
          'callsign': 'TheUser',
        },
      },
    })

  def test_to_primitive_no_actor(self):
    testee = HumanConnectionEstablishedEvent(
      HumanConnectionEstablishedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        actor=None,
      ),
    )
    primitive = testee.to_primitive()
    self.assertIsNone(primitive['data']['actor'])

  def test_from_primitive(self):
    testee = HumanConnectionEstablishedEvent(
      HumanConnectionEstablishedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        actor=HumanActor(
          callsign="TheUser",
        ),
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionEstablishedEvent.from_primitive(testee.to_primitive()),
    )

  def test_from_primitive_no_actor(self):
    testee = HumanConnectionEstablishedEvent(
      HumanConnectionEstablishedInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        actor=None,
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionEstablishedEvent.from_primitive(testee.to_primitive()),
    )


class HumanConnectionEstablishedLightEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionEstablishedLightEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionEstablishedLightEvent"),
      HumanConnectionEstablishedLightEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionEstablishedLightEvent(
      HumanConnectionEstablishedLightInfo(
        actor=HumanActor("TheUser"),
        time=datetime.time(23, 45, 59),
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionEstablishedLightEvent',
      'verbose_name': 'Human connection with server established (light)',
      'help_text': None,
      'data': {
        'actor': {'callsign': 'TheUser'},
        'time': '23:45:59',
      },
    })

  def test_from_primitive(self):
    testee = HumanConnectionEstablishedLightEvent(
      HumanConnectionEstablishedLightInfo(
        actor=HumanActor("TheUser"),
        time=datetime.time(23, 45, 59),
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionEstablishedLightEvent.from_primitive(testee.to_primitive()),
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
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        reason="You have been kicked from the server.",
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionLostEvent',
      'verbose_name': 'Human connection with server lost',
      'help_text': None,
      'data': {
        'address': {'host': '127.0.0.1', 'port': 21000},
        'channel_no': 1,
        'reason': "You have been kicked from the server.",
      },
    })

  def test_to_primitive_no_reason(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        reason=None,
      ),
    )
    primitive = testee.to_primitive()
    self.assertIsNone(primitive['data']['reason'])

  def test_from_primitive(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        reason="You have been kicked from the server.",
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionLostEvent.from_primitive(testee.to_primitive()),
    )

  def test_from_primitive_no_reason(self):
    testee = HumanConnectionLostEvent(
      HumanConnectionLostInfo(
        address=ConnectionAddress(host="127.0.0.1", port=21000),
        channel_no=1,
        reason=None,
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionLostEvent.from_primitive(testee.to_primitive()),
    )


class HumanConnectionLostLightEventTestCase(unittest.TestCase):

  def test_derives_from_HumanConnectionEvent(self):
    self.assertTrue(issubclass(
      HumanConnectionLostLightEvent,
      HumanConnectionEvent,
    ))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanConnectionLostLightEvent"),
      HumanConnectionLostLightEvent,
    )

  def test_to_primitive(self):
    testee = HumanConnectionLostLightEvent(
      HumanConnectionLostLightInfo(
        actor=HumanActor("TheUser"),
        time=datetime.time(23, 45, 59),
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'connection',
      'name': 'HumanConnectionLostLightEvent',
      'verbose_name': 'Human connection with server lost (light)',
      'help_text': None,
      'data': {
        'actor': {'callsign': 'TheUser'},
        'time': '23:45:59',
      },
    })

  def test_from_primitive(self):
    testee = HumanConnectionLostLightEvent(
      HumanConnectionLostLightInfo(
        actor=HumanActor("TheUser"),
        time=datetime.time(23, 45, 59),
      ),
    )
    self.assertEqual(
      testee,
      HumanConnectionLostLightEvent.from_primitive(testee.to_primitive()),
    )
