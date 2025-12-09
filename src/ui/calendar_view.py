from tkinter import ttk, constants, Text, END
import calendar as pycalendar
from datetime import datetime
from tkinter import *
from services.calendar_service import calendar_service
from services.event_service import event_service

class CalendarItemView:
    def __init__(self, root, calendar, event_form=None):
        self._root = root
        self._calendar = calendar
        self._frame = None
        self._event_form=event_form
        self._user = calendar_service.get_current_user()
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize_calendar_item(self):
        item_frame = ttk.Frame(master=self._frame)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.BOTH, expand=True)
        
        now = datetime.now()
        now_month = now.month
        now_year = now.year
        month_name = pycalendar.month_name[now_month]
        ttk.Label(
            item_frame,
            text=f"{month_name} {now_year}",
            font=("TkDefaultFont", 12, "bold")
        ).grid(row=0, column=0, columnspan=7, pady=(0, 10))
        month_dates = pycalendar.monthcalendar(now.year, now.month)
        for col, day_name in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
            ttk.Label(item_frame, text=day_name).grid(row=1, column=col)
        
        for row, week in enumerate(month_dates):
            for col, day in enumerate(week):
                if day == 0:
                    continue
                date = f"{now_year}-{now_month:02d}-{day:02d}"
                events = self._get_events_for_date(date)
                label_text = f"{day}" + (" *" if events else "")
                button = ttk.Button(
                    item_frame,
                    text= label_text,
                    command= lambda d=day: self._click_date(d, now.month, now.year)
                )
                button.grid(row=row+2, column=col, sticky="nsew", padx=2, pady=2)

    def _get_events_for_date(self, date):
        event_service._user = self._user
        events = event_service._event_repo.find_all()
        # matching = [event.content for event in events if getattr(event, "date", "") == date]
        # print(f"Events for {date}: {matching}")
        return [event.content for event in events if getattr(event, "date", "")==date]

    def _click_date(self, day, month, year):
        date = f"{year}-{month:02d}-{day:02d}"
        if self._event_form:
            self._event_form(date)
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_calendar_item()

class CalendarView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._user = calendar_service.get_current_user()
        self._frame = None
        self._calendar_frame = None
        self._calendar_view = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Welcome {self._user.username}! <3"
        )
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        
    def _initialize_calendar(self):
        if self._calendar_view:
            self._calendar_view.destroy()
        calendar = calendar_service.get_calendar()
        self._calendar_view = CalendarItemView(
            self._calendar_frame,
            calendar,
            event_form = self._open_event_form
        )
        self._calendar_view.pack()
    
    def _open_event_form(self, date):
        frame_top = Toplevel(self._frame)
        frame_top.title("Add Event")
        ttk.Label(frame_top, text=f"Event on date: {date}").pack()
        
        ttk.Label(frame_top, text="Event name:").pack()
        entry_name = ttk.Entry(frame_top)
        entry_name.pack()
        
        ttk.Label(frame_top, text="Event description:").pack()
        description_text = Text(frame_top, height=4, width=40)
        description_text.pack()
        def create_event():
            event_name = entry_name.get()
            event_description = description_text.get("1.0", "end").strip()
            if event_name:
                event_service._user = self._user
                content = f"{event_name}:{event_description}" if event_description else event_name
                # print("Saving event for", date, "content:", content)
                event_service.create_event(content=content, date=date)
                frame_top.destroy()
                self._initialize_calendar()
        ttk.Button(frame_top, text="Create", command=create_event).pack()
        ttk.Button(frame_top, text="Cancel", command=frame_top.destroy).pack()

        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._calendar_frame = ttk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_calendar()
        self._calendar_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
        
        