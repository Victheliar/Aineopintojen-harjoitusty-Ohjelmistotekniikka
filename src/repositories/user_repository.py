from entitites.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row["username"], row["password"] if row else None)

class UserRepository:
    # Käyttäjiin liittyvät tietokantaoperaatiot <3
    def __init__(self, connection):
        self._connection = connection
    
    def find_by_username(self, username):
        # Palauttaa käyttäjän käyttäjätunnuksen perusteella
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM Users WHERE Username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return get_user_by_row(row)
    
    def create(self, user):
        # tallenna uusi käyttäjä tietokantaan
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user
    
user_repository = UserRepository(get_database_connection())