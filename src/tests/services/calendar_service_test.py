import unittest
from entities.user import User
from entities.event import Event
from services.calendar_service import CalendarService, InvalidCredentialsError, UsernameExistsError
from services.event_service import EventService


class FakeEventRepo:
    def __init__(self, events=None):
        self.events = events or []

    def find_all(self):
        return self.events

    def find_by_username(self, username):
        user_events = filter(
            lambda event: event.user and event.user.username == username, self.events)
        return list(user_events)

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


class TestCalendarService(unittest.TestCase):
    def setUp(self):
        self.event_service = EventService(FakeEventRepo(), FakeUserRepo())
        self.calendar_service = CalendarService(FakeUserRepo(), FakeCalendarRepo())
        self.event_a = Event(content="testing a", date="2025-12-09")
        self.event_b = Event(content="testing b", date="2025-12-08")
        self.user_vici = User("vici", "testi123")

    def login_user(self, user):
        self.calendar_service.create_user(user.username, user.password)
    
    def test_create_calendar(self):
        self.login_user(self.user_vici)
        
        self.calendar_service.create_calendar()
        calendar = self.calendar_service.get_calendar()
        self.assertIsNotNone(calendar)
        self.assertEqual(calendar.user.username, self.user_vici.username)

    def test_login_with_valid_username_and_password(self):
        self.calendar_service.create_user(
            self.user_vici.username,
            self.user_vici.password
        )
        user = self.calendar_service.login(
            self.user_vici.username,
            self.user_vici.password
        )
        self.assertEqual(user.username, self.user_vici.username)
    
    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(InvalidCredentialsError, lambda: self.calendar_service.login("testing", "invalid"))
    
    def test_get_current_user(self):
        self.login_user(self.user_vici)
        current_user = self.calendar_service.get_current_user()
        self.assertEqual(current_user.username, self.user_vici.username)
    
    def test_create_user_with_non_existing_username(self):
        username = self.user_vici.username
        password = self.user_vici.password
        
        self.calendar_service.create_user(username, password)
        users = self.calendar_service.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_vici.username
        self.calendar_service.create_user(username, "something")
        
        self.assertRaises(UsernameExistsError, lambda: self.calendar_service.create_user(username, "random"))
        
    def test_logout(self):
        self.login_user(self.user_vici)
        self.calendar_service.logout()
        user = self.calendar_service.get_current_user()
        self.assertIsNone(user)
    
    def test_user_not_logged_in(self):
        calendar = self.calendar_service.get_calendar()
        self.assertEqual(calendar, [])