from ui.create_account_view import CreateAccountView

class UI:
    # Sovelluksen käyttöliittymä
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        # Käynnistää käyttöliittymän
        self._show_create_user_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateAccountView(self._root)
        self._current_view.pack()