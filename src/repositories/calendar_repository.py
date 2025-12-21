from pathlib import Path
from entities.calendar import Calendar
from repositories.user_repository import user_repository
from repositories.csv_base_repository import CSVBaseRepository
from config import CALENDAR_FILE_PATH


class CalendarRepository(CSVBaseRepository):

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        calendars = []
        self._ensure_file_exists()
        rows = self._read_csv_file()

        for parts in rows:
            calendar_id = parts[0]
            username = parts[1]

            user = user_repository.find_by_username(
                username) if username else None
            calendars.append(Calendar(user, calendar_id))

        return calendars

    def _write(self, calendars):
        self._ensure_file_exists()
        with open(self._file_path, "w", encoding="utf-8") as file:
            for calendar in calendars:
                username = calendar.user.username if calendar.user else ""
                row = f"{calendar.id};{username}"
                file.write(row+"\n")

    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        return next(
            (calendar for calendar in self.find_all()
             if calendar.user and getattr(calendar.user, "username", None) == username),
            None)

    def create(self, calendar):
        calendars = self.find_all()
        calendars.append(calendar)
        self._write(calendars)
        return calendar

    def delete_all(self):
        self._write([])


calendar_repository = CalendarRepository(CALENDAR_FILE_PATH)
