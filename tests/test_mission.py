import datetime
import unittest

from pathlib import Path

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.mission import MissionLoadedInfo
from il2fb.ds.events.definitions.mission import MissionStartedInfo
from il2fb.ds.events.definitions.mission import MissionEndedInfo

from il2fb.ds.events.definitions.mission import MissionStatusEvent
from il2fb.ds.events.definitions.mission import MissionLoadedEvent
from il2fb.ds.events.definitions.mission import MissionStartedEvent
from il2fb.ds.events.definitions.mission import MissionEndedEvent

from il2fb.ds.events.definitions import registry


class MissionStatusEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(MissionStatusEvent, Event))


class MissionLoadedEventTestCase(unittest.TestCase):

  def test_derives_from_MissionStatusEvent(self):
    self.assertTrue(issubclass(MissionLoadedEvent, MissionStatusEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("MissionLoadedEvent"),
      MissionLoadedEvent,
    )

  def test_to_primitive(self):
    testee = MissionLoadedEvent(
      MissionLoadedInfo(
        timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
        file_path=Path('net/dogfight/1596469535.mis'),
      ),
    )
    self.assertEqual(testee.to_primitive(), {
      'category': 'mission',
      'name': 'MissionLoadedEvent',
      'verbose_name': 'Mission loaded',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'file_path': 'net/dogfight/1596469535.mis',
      },
    })

  def test_from_primitive(self):
    testee = MissionLoadedEvent(
      MissionLoadedInfo(
        timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
        file_path=Path('net/dogfight/1596469535.mis'),
      ),
    )
    self.assertEqual(
      testee,
      MissionLoadedEvent.from_primitive(testee.to_primitive()),
    )


class MissionStartedEventTestCase(unittest.TestCase):

  def test_derives_from_MissionStatusEvent(self):
    self.assertTrue(issubclass(MissionStartedEvent, MissionStatusEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("MissionStartedEvent"),
      MissionStartedEvent,
    )

  def test_to_primitive(self):
    testee = MissionStartedEvent(MissionStartedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'mission',
      'name': 'MissionStartedEvent',
      'verbose_name': 'Mission started',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
      },
    })

  def test_from_primitive(self):
    testee = MissionStartedEvent(MissionStartedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
    ))
    self.assertEqual(
      testee,
      MissionStartedEvent.from_primitive(testee.to_primitive()),
    )


class MissionEndedEventTestCase(unittest.TestCase):

  def test_derives_from_MissionStatusEvent(self):
    self.assertTrue(issubclass(MissionEndedEvent, MissionStatusEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("MissionEndedEvent"),
      MissionEndedEvent,
    )

  def test_to_primitive(self):
    testee = MissionEndedEvent(MissionEndedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'mission',
      'name': 'MissionEndedEvent',
      'verbose_name': 'Mission ended',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
      },
    })

  def test_from_primitive(self):
    testee = MissionEndedEvent(MissionEndedInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
    ))
    self.assertEqual(
      testee,
      MissionEndedEvent.from_primitive(testee.to_primitive()),
    )
