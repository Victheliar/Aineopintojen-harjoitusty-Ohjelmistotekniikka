import unittest
from entitites.user import User
from services.calendar_service import InvalidCredentialsError, UsernameExistsError

class FakeUserRepo:
    def __init__(self, users=None):
        pass
    