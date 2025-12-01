from tkinter import ttk, constants
from services.calendar_service import calendar_service

class CalendarView:
    def __init__(self, root):
        self._root = root
        self._user = calendar_service.get_current_user()
        self._frame = None
        self._calendar_frame = None
        self._initialize()
    
    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Welcome {self._user.username}! ✨"
        )
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._calendar_frame = ttk.Frame(master=self._frame)
        self._initialize_header()