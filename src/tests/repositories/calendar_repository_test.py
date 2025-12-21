import unittest
from repositories.calendar_repository import calendar_repository
from repositories.user_repository import user_repository
from entities.calendar import Calendar
from entities.user import User

class TestCalendarRepository(unittest.TestCase):
    def setUp(self):
        calendar_repository.delete_all()
        user_repository.delete_all()
        
        self.user_vici = User("vici", "vici123")
        user_repository.create(self.user_vici)
        self.user_testi = User("testi", "testitesti")
        user_repository.create(self.user_testi)

        self.calendar_vici = Calendar(user=self.user_vici)
        self.calendar_testi = Calendar(user=self.user_testi)
    
    def test_create(self):
        calendar_repository.create(self.calendar_vici)
        calendars = calendar_repository.find_all()
        self.assertEqual(len(calendars), 1)
        self.assertEqual(calendars[0].user.username, self.user_vici.username)
        
    def test_find_all(self):
        calendar_repository.create(self.calendar_vici)
        calendar_repository.create(self.calendar_testi)
        calendars = calendar_repository.find_all()
        
        self.assertEqual(len(calendars), 2)
        self.assertEqual(calendars[0].user.username, self.user_vici.username)
        self.assertEqual(calendars[1].user.username, self.user_testi.username)
    
    def test_find_by_username(self):
        calendar_repository.create(self.calendar_vici)
        calendar_repository.create(self.calendar_testi)
        
        vici_cal = calendar_repository.find_by_username(self.user_vici.username)
        self.assertEqual(vici_cal.user.username, self.user_vici.username)
        
        testi_cal = calendar_repository.find_by_username(self.user_testi.username)
        self.assertEqual(testi_cal.user.username, self.user_testi.username)
        