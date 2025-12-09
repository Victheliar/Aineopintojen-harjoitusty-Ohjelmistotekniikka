import uuid

class Event:
    def __init__(self, content, date, user=None, event_id=None, calendar_id=None):
        self.content = content
        self.user = user
        self.id = event_id or str(uuid.uuid4())
        self.calendar_id = calendar_id
        self.date = date