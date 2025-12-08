import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

CALENDAR_FILENAME = os.getenv("CALENDAR_FILENAME") or "calendar.csv"
CALENDAR_FILE_PATH = os.path.join(dirname, "..", "data", CALENDAR_FILENAME)

EVENT_FILENAME = os.getenv("EVENT_FILENAME") or "event.csv"
EVENT_FILE_PATH = os.path.join(dirname, "..", "data", EVENT_FILENAME)