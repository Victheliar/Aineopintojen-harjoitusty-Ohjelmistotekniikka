class User:
    """
    Yksittäistä käyttäjää kuvaava luokka.
    Attributes:
        username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
