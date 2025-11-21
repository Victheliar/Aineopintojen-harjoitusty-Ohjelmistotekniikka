from tkinter import ttk, StringVar, constants
from services.calendar_service import calendar_service, InvalidCredentialsError


class LoginView:
    # Kirjautuminen
    def __init__(self, root, handle_show_create_account_view):
        self._root = root
        self._handle_show_create_account_view = handle_show_create_account_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_var = None
        self._error_label = None

        self._initialize()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        try:
            calendar_service.login(username, password)
        except InvalidCredentialsError:
            self._show_error("Invalid username or password!")

    def _show_error(self, message):
        self._error_var.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def pack(self):
        # Näyttää näkymän
        self._frame.pack(fill=constants.X)

    def destroy(self):
        # Tuhoaa näkymän
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)
        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        create_account_button = ttk.Button(
            master=self._frame,
            text="Create new account",
            command=self._handle_show_create_account_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_account_button.grid(padx=5, pady=5, sticky=constants.EW)
        self._hide_error()
