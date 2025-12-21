import unittest
from repositories.calendar_repository import calendar_repository
from repositories.user_repository import user_repository
from repositories.event_repository import event_repository
from entities.calendar import Calendar
from entities.user import User
from entities.event import Event


class TestEventRepository(unittest.TestCase):
    def setUp(self):
        event_repository.delete_all()
        user_repository.delete_all()
        calendar_repository.delete_all()

        self.user_vici = User("vici", "testi123")
        user_repository.create(self.user_vici)
        self.user_testi = User("testi", "testitesti")
        user_repository.create(self.user_testi)
        
        self.calendar_vici = Calendar(self.user_vici)
        calendar_repository.create(self.calendar_vici)
        self.calendar_testi = Calendar(self.user_testi)
        calendar_repository.create(self.calendar_testi)
        
        self.event_a = Event(content="testing a", date="2025-12-09", user=self.user_vici)
        self.event_b = Event(content="testing b", date="2025-12-08", user=self.user_testi)
        

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
        event_repository.create(
            Event(content="testing a", date="2025-12-09", user=self.user_vici))
        event_repository.create(
            Event(content="testing b", date="2025-12-08", user=self.user_testi))

        vici_events = event_repository.find_by_username(
            self.user_vici.username)
        self.assertEqual(len(vici_events), 1)
        self.assertEqual(vici_events[0].content, "testing a")

        testi_events = event_repository.find_by_username(
            self.user_testi.username)
        self.assertEqual(len(testi_events), 1)
        self.assertEqual(testi_events[0].content, "testing b")

    def test_find_user_events_by_date(self):
        event_repository.create(
            Event(content="testing a", date="2025-12-09", user=self.user_vici))
        event_repository.create(
            Event(content="testing b", date="2025-12-08", user=self.user_vici))
        
        day_events = event_repository.find_user_events_by_date("2025-12-09", self.user_vici.username)
        self.assertEqual(len(day_events), 1)
        self.assertEqual(day_events[0], "testing a")