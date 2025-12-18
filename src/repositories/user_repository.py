from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """
    Käyttäjiin liittyvät tietokantaoperaatiot
    """

    def __init__(self, connection):
        """
        Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self._connection = connection

    def find_by_username(self, username):
        """
        Palauttaa käyttäjän käyttäjätunnuksen perusteella

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.

        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omaava käyttäjä on tietokannassa.
            Muutoin None.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM Users WHERE Username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        """tallenna uusi käyttäjä tietokantaan

        Args:
            user: Tallennettava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttäjä User-oliona.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def delete_all(self):
        """Tyhjentää tietokannan taulun Users eli poistaa kaikki käyttäjät"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Users")
        self._connection.commit()

    def find_all(self):
        """Etsii ja palauttaa kaikki käyttäjät tietokannasta

        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))


user_repository = UserRepository(get_database_connection())
