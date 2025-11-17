from entitites.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class UsernameExistsError(Exception):
    pass

class CalendarService:
    # Sovelluslogiikkaa <3
    def __init__(
        self,
        user_repo = default_user_repository        
                 ):
    
        self._user = None
        self._user_repo = user_repo
    
    def create_user(self, username, password, login=True):
        existing_user = self._user_repo.find_by_username(username)
        
        if existing_user:
            raise UsernameExistsError(f"Username {username} is taken :(")
        
        user = self._user_repo.create(User(username, password))
        return user

calendar_service = CalendarService()
    