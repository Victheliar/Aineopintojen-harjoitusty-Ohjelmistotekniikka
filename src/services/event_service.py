from entities.event import Event
from entities.user import User

from repositories.event_repository import(
    event_repository as default_event_repo
)

from repositories.user_repository import(
    user_repository as default_user_repo
)

from repositories.calendar_repository import(
    calendar_repository as default_calendar_repo
)

class EventService:
    def __init__(
        self,
        event_repo = default_event_repo,
        user_repo = default_user_repo,
        calendar_repo = default_calendar_repo
        ):
        self._user = None
        self._event_repo = event_repo
        self._user_repo = user_repo
        self._calendar_repo = calendar_repo
    
    def create_event(self, content, date):
        calendar = self._calendar_repo.find_by_username(self._user.username)
        calendar_id = calendar.id
        event = Event(content=content, date=date, user=self._user, calendar_id=calendar_id)
        return self._event_repo.create(event)
    
event_service = EventService()