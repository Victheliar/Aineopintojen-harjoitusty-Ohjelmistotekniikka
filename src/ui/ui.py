from ui.create_account_view import CreateAccountView
from ui.login_view import LoginView

class UI:
    # Sovelluksen käyttöliittymä
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        # Käynnistää käyttöliittymän
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateAccountView(self._root, self._show_login_view)
        self._current_view.pack()
    
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_create_user_view)
        self._current_view.pack()