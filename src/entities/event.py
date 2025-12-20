import uuid


class Event:
    """
    Yksittäistä tapahtumaa kuvaava luokka

    Attributes:
        content: Merkkijonoarvo, joka kuvaa tapahtuman kuvausta.
        date: YYY-MM-DD-muotoinen merkkijonoarvo, joka kuvastaa päivämäärää.
        user: User-olio, joka kuvaa kalenterin omistajaa.
        event_id: Merkkijonoarvo, joka kuvaa tapahtuman id:tä.
        calendar_id: Merkkijonoarvo, joka kuvaa kalenterin id:tä
    """

    def __init__(self, *, content, date, user=None, event_id=None, calendar_id=None):
        self.content = content
        self.user = user
        self.id = event_id or str(uuid.uuid4())
        self.calendar_id = calendar_id
        self.date = date
