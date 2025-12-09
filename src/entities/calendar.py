import uuid
from datetime import datetime
import calendar

class Calendar:
    """
    Yksittäistä kalenteria kuvaava luokka
    
    Attributes:
        user: User-olio, joka kuvaa kalenterin omistajaa.
        calendar_id: Merkkijonarvo, joka kuvaa kalenterin id:tä
    """
    def __init__(self, user=None, calendar_id=None):
        self.user = user
        self.id = calendar_id or str(uuid.uuid4())
        self.year = datetime.now().year
        self.calendar = calendar.calendar(self.year)
