from pathlib import Path
from entities.event import Event
from repositories.calendar_repository import calendar_repository
from repositories.user_repository import user_repository
from config import EVENT_FILE_PATH


class EventRepository:
    """Tapahtumiin liittyvistä tietokantaoperaatioista vastaava luokka"""

    def __init__(self, file_path):
        """
        Luokan konstruktori.

        Args:
            file_path: Polku CSV-tiedostoon, johon tapahtumat tallennetaan.
        """
        self._file_path = file_path

    def find_all(self):
        """
        Palauttaa kaikki tapahtumat

        Returns:
            Palauttaa listan Event-olioita.
        """
        return self._read()

    def find_events_by_date(self, date):
        events = self.find_all()
        return [event.content for event in events if getattr(event, "date", "")==date]

    def _read(self):
        events = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                event_id = parts[0]
                content = parts[1]
                date = parts[2]
                username = parts[3]
                calendar_id = parts[4]

                user = user_repository.find_by_username(
                    username) if username else None

                events.append(
                    Event(content, date, user, event_id, calendar_id))
            return events

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def find_by_username(self, username):
        """
        Palauttaa käyttäjän tapahtumat.

        Args:
            username: Käyttäjän käyttäjätunnus, jonka tapahtumat palautetaan

        Returns:
            Palauttaa listan Event-olioita.
        """
        events = self.find_all()
        user_events = filter(
            lambda event: event.user and event.user.username == username, events)
        return list(user_events)

    def create(self, event):
        """
        Tallentaa tapahtuman tietokantaan.

        Args:
            event: Tallennettava tapahtuma Event-oliona

        Returns:    
            Tallennettu tapahtuma Event-oliona.
        """
        events = self.find_all()
        events.append(event)
        self._write(events)
        return event

    def _write(self, events):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for event in events:
                username = getattr(event.user, "username",
                                   "") if event.user else ""
                calendar = calendar_repository.find_by_username(username)
                calendar_id = calendar.id
                row = f"{event.id};{event.content};{event.date};{username};{calendar_id}"
                file.write(row+"\n")

    def delete_all(self):
        """
        Poistaa kaikki tapahtumat
        """
        self._write([])


event_repository = EventRepository(EVENT_FILE_PATH)
