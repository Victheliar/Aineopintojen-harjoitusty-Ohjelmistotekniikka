import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_vici = User("vici", "vici123")
        self.user_testi = User("testi", "testi123")

    def test_create(self):
        user_repository.create(self.user_vici)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_vici.username)

    def test_find_all(self):
        user_repository.create(self.user_vici)
        user_repository.create(self.user_testi)
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)
