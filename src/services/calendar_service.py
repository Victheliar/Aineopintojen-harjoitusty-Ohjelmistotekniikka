from entitites.user import User
from entitites.calendar import Calendar
from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.calendar_repository import (
    calendar_repository as default_calendar_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class CalendarService:
    # Sovelluslogiikkaa <3
    def __init__(
        self,
        user_repo=default_user_repository,
        calendar_repo=default_calendar_repository
    ):

        self._user = None
        self._user_repo = user_repo
        self._calendar_repo = calendar_repo

    def create_user(self, username, password, login=True):
        existing_user = self._user_repo.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} is taken :(")

        user = self._user_repo.create(User(username, password))
        if login:
            self._user = user
            self.create_calendar()
        return user

    def login(self, username, password):
        user = self._user_repo.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password!")
        self._user = user
        self.get_calendar()
        return user

    def get_current_user(self):
        return self._user

    def create_calendar(self):
        existing_calendar = self._calendar_repo.find_by_username(self._user.username)
        if existing_calendar:
            return existing_calendar
        calendar = Calendar(user=self._user)
        return self._calendar_repo.create(calendar)

    def get_calendar(self):
        if not self._user:
            return []
        calendar = self._calendar_repo.find_by_username(self._user.username)
        return calendar

calendar_service = CalendarService()
