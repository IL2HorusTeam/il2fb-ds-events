import datetime
import unittest

from il2fb.commons.actors import HumanActor
from il2fb.commons.actors import HumanAircraftCrewMemberActor

from il2fb.commons.spatial import Point3D

from il2fb.ds.events.definitions.base import Event

from il2fb.ds.events.definitions.seats import HumanOccupiedCrewMemberSeatEvent
from il2fb.ds.events.definitions.seats import HumanOccupiedCrewMemberSeatInfo

from il2fb.ds.events.definitions import registry


class HumanOccupiedCrewMemberSeatEventTestCase(unittest.TestCase):

  def test_derives_from_Event(self):
    self.assertTrue(issubclass(HumanOccupiedCrewMemberSeatEvent, Event))

  def test_is_registered(self):
    self.assertEqual(
      registry.get_class_by_name("HumanOccupiedCrewMemberSeatEvent"),
      HumanOccupiedCrewMemberSeatEvent,
    )

  def test_to_primitive(self):
    testee = HumanOccupiedCrewMemberSeatEvent(HumanOccupiedCrewMemberSeatInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
      target=HumanAircraftCrewMemberActor(
        callsign="TheUser",
        aircraft="P-39D2",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(testee.to_primitive(), {
      'category': 'seats',
      'name': 'HumanOccupiedCrewMemberSeatEvent',
      'verbose_name': 'Human occupied crew member seat',
      'help_text': None,
      'data': {
        'timestamp': '2020-12-31T23:45:59',
        'actor': {
          'callsign': 'TheUser',
        },
        'target': {
          'callsign': 'TheUser',
          'aircraft': 'P-39D2',
          'member_index': 0,
        },
        'pos': {'x': 71903.14, 'y': 41619.023, 'z': 80.754},
      },
    })

  def test_from_primitive(self):
    testee = HumanOccupiedCrewMemberSeatEvent(HumanOccupiedCrewMemberSeatInfo(
      timestamp=datetime.datetime(2020, 12, 31, 23, 45, 59),
      actor=HumanActor(
        callsign="TheUser",
      ),
      target=HumanAircraftCrewMemberActor(
        callsign="TheUser",
        aircraft="P-39D2",
        member_index=0,
      ),
      pos=Point3D(71903.14, 41619.023, 80.754),
    ))
    self.assertEqual(
      testee,
      HumanOccupiedCrewMemberSeatEvent.from_primitive(testee.to_primitive()),
    )
