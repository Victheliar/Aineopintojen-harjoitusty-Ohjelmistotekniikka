from tkinter import ttk, constants
from services.calendar_service import calendar_service

class CalendarItemView:
    def __init__(self, root, calendar):
        self._root = root
        self._calendar = calendar
        self._frame = None
        self._initialize()
    
    def _initialize_calendar(self, calendar):
        pass
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_calendar(self._calendar)

class CalendarView:
    def __init__(self, root):
        self._root = root
        self._user = calendar_service.get_current_user()
        self._frame = None
        self._calendar_frame = None
        self._calendar_view = None
        self._initialize()
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Welcome {self._user.username}! ✨"
        )
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        
    def _initialize_calendar(self):
        if self._calendar_view:
            self._calendar_view.destroy()
        calendar = calendar_service.get_calendar()
        self._calendar_view = CalendarItemView(
            
        )
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._calendar_frame = ttk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_calendar()