import unittest
from entities.event import Event
from entities.calendar import Calendar
from entities.user import User
from services.event_service import EventService
from services.calendar_service import CalendarService

class FakeEventRepo:
    def __init__(self, events=None):
        self.events = events or []

    def find_all(self):
        return self.events

    def find_by_username(self, username):
        user_events = filter(
            lambda event: event.user and event.user.username == username, self.events)
        return list(user_events)
    
    def find_user_events_by_date(self, date, username):
        user_events = self.find_by_username(username)
        date_events = filter(
            lambda event: event.date and event.date == date, user_events
        )
        return list(date_events)

    def create(self, event):
        self.events.append(event)
        return event

    def delete_all(self):
        self.events = []


class FakeUserRepo:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class FakeCalendarRepo:
    def __init__(self, calendars=None):
        self.calendars = calendars or []

    def find_all(self):
        return self.calendars

    def find_by_username(self, username):
        user_cals = filter(
            lambda cal: cal.user and cal.user.username == username, self.calendars)
        matching_cals_list = list(user_cals)
        return matching_cals_list[0] if len(matching_cals_list)>0 else None

    def create(self, calendar):
        self.calendars.append(calendar)
        return calendar

class TestEventService(unittest.TestCase):
    def setUp(self):
        user_repo = FakeUserRepo()
        calendar_repo = FakeCalendarRepo()
        event_repo = FakeEventRepo()
        self.event_service = EventService(event_repo, user_repo, calendar_repo)
        self.calendar_service = CalendarService(user_repo, calendar_repo)
        
        self.user_vici = User("vici", "vici123")
        self.calendar_vici = Calendar(self.user_vici)
        calendar_repo.create(self.calendar_vici)
    
    def login_user(self, user):
        self.calendar_service.create_user(user.username, user.password)
        self.calendar_service.login(user.username, user.password)
        self.calendar_service.create_calendar()
        current_user = self.calendar_service.get_current_user()
        self.event_service.set_current_user(current_user)
        
    
    def test_create_event(self):
        self.login_user(self.user_vici)
        self.event_service.create_event("testing", "2025-12-21")
        events = self.event_service.get_events_by_date("2025-12-21", self.user_vici.username)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].content, "testing")
        self.assertEqual(events[0].user.username, self.user_vici.username)
    
    def test_get_events_by_date(self):
        self.login_user(self.user_vici)
        self.event_service.create_event(content="testing a", date="2025-12-21")
        self.event_service.create_event(content="testing b", date="2025-12-20")
        events = self.event_service.get_events_by_date("2025-12-21", self.user_vici.username)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].date,"2025-12-21")
        events = self.event_service.get_events_by_date("2025-12-20", self.user_vici.username)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].date,"2025-12-20")
        