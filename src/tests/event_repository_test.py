import unittest
from repositories.calendar_repository import calendar_repository
from repositories.user_repository import user_repository
from repositories.event_repository import event_repository
from entities.calendar import Calendar
from entities.user import User
from entities.event import Event


class TestCalendarRepository(unittest.TestCase):
    def setUp(self):
        event_repository.delete_all()
        user_repository.delete_all()

        self.event_a = Event("testing a", "2025-12-09")
        self.event_b = Event("testing b", "2025-12-08")
        self.user_vici = User("vici", "testi123")
        self.user_testi = User("testi", "testitesti")

    def test_create(self):
        event_repository.create(self.event_a)
        events = event_repository.find_all()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].content, self.event_a.content)

    def test_find_all(self):
        event_repository.create(self.event_a)
        event_repository.create(self.event_b)
        events = event_repository.find_all()

        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].content, self.event_a.content)
        self.assertEqual(events[1].content, self.event_b.content)

    def test_find_by_username(self):
        vici = user_repository.create(self.user_vici)
        testi = user_repository.create(self.user_testi)
        event_repository.create(
            Event(content="testing a", date="2025-12-09", user=vici))
        event_repository.create(
            Event(content="testing b", date="2025-12-08", user=testi))

        vici_events = event_repository.find_by_username(
            self.user_vici.username)
        self.assertEqual(len(vici_events), 1)
        self.assertEqual(vici_events[0].content, "testing a")

        testi_events = event_repository.find_by_username(
            self.user_testi.username)
        self.assertEqual(len(testi_events), 1)
        self.assertEqual(testi_events[0].content, "testing b")
