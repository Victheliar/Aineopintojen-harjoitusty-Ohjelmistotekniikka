from entitites.event import Event
from entitites.user import User

from repositories.event_repository import(
    event_repository as default_event_repo
)

from repositories.user_repository import(
    user_repository as default_user_repo
)

class EventService:
    def __init__(
        self,
        event_repo = default_event_repo,
        user_repo = default_user_repo
        ):
        self._user = None