import unittest
from entities.user import User
from services.calendar_service import InvalidCredentialsError, UsernameExistsError


class FakeUserRepo:
    def __init__(self, users=None):
        pass
