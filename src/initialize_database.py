from database_connection import get_database_connection

def drop_tables(connection):
    # Posta taulut
    cursor = connection.cursor()
    cursor.execute("""
                   DROP TABLE IF EXISTS Users;
                   """)
    connection.commit()

def create_tables(connection):
    # Luo taulut tietokantaan <3
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE Users (
                       username TEXT PRIMARY KEY,
                       password TEXT
                       );
                   """)
    connection.commit()
    
def initialize_database():
    # Alusta tietokanta
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    
if __name__ == "__main__":
    initialize_database()