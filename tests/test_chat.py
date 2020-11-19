import unittest

from il2fb.commons.actors import HumanActor

from il2fb.ds.events.definitions.chat import ChatMessage
from il2fb.ds.events.definitions.chat import HumanChatMessage

from il2fb.ds.events.definitions.chat import ChatMessageEvent
from il2fb.ds.events.definitions.chat import ServerChatMessageEvent
from il2fb.ds.events.definitions.chat import SystemChatMessageEvent
from il2fb.ds.events.definitions.chat import HumanChatMessageEvent

from il2fb.ds.events.definitions import registry


class ServerChatMessageEventTestCase(unittest.TestCase):

  def test_derives_from_ChatMessageEvent(self):
    self.assertTrue(issubclass(ServerChatMessageEvent, ChatMessageEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("ServerChatMessageEvent"),
      ServerChatMessageEvent,
    )

  def test_to_primitive(self):
    testee = ServerChatMessageEvent(ChatMessage("text"))
    self.assertEqual(testee.to_primitive(), {
      'category': 'chat',
      'name': 'ServerChatMessageEvent',
      'verbose_name': 'Chat message from server',
      'help_text': None,
      'data': {'msg': 'text'},
    })

  def test_from_primitive(self):
    testee = ServerChatMessageEvent(ChatMessage("text"))
    self.assertEqual(
      testee,
      ServerChatMessageEvent.from_primitive(testee.to_primitive()),
    )


class SystemChatMessageEventTestCase(unittest.TestCase):

  def test_derives_from_ChatMessageEvent(self):
    self.assertTrue(issubclass(SystemChatMessageEvent, ChatMessageEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("SystemChatMessageEvent"),
      SystemChatMessageEvent,
    )

  def test_to_primitive(self):
    testee = SystemChatMessageEvent(ChatMessage("text"))
    self.assertEqual(testee.to_primitive(), {
      'category': 'chat',
      'name': 'SystemChatMessageEvent',
      'verbose_name': 'Chat message from system',
      'help_text': None,
      'data': {'msg': 'text'},
    })

  def test_from_primitive(self):
    testee = SystemChatMessageEvent(ChatMessage("text"))
    self.assertEqual(
      testee,
      SystemChatMessageEvent.from_primitive(testee.to_primitive()),
    )


class HumanChatMessageEventTestCase(unittest.TestCase):

  def test_derives_from_ChatMessageEvent(self):
    self.assertTrue(issubclass(HumanChatMessageEvent, ChatMessageEvent))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanChatMessageEvent"),
      HumanChatMessageEvent,
    )

  def test_to_primitive(self):
    testee = HumanChatMessageEvent(HumanChatMessage("text", HumanActor("johndoe")))
    self.assertEqual(testee.to_primitive(), {
      'category': 'chat',
      'name': 'HumanChatMessageEvent',
      'verbose_name': 'Chat message from human',
      'help_text': None,
      'data': {'msg': 'text', 'actor': {'callsign': 'johndoe'}},
    })

  def test_from_primitive(self):
    testee = HumanChatMessageEvent(HumanChatMessage("text", HumanActor("johndoe")))
    self.assertEqual(
      testee,
      HumanChatMessageEvent.from_primitive(testee.to_primitive()),
    )
