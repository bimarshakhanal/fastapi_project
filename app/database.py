import sqlite3

DATABASE_URI = "data.db"


def create_connection():
    """Connects to the SQLite database and returns a connection object."""
    connection = sqlite3.connect(DATABASE_URI)
    return connection


def create_table(connection):
    """
    Creates the 'employees' table in the database based on the Employee model.
    """
    cursor = connection.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS employees (
          id TEXT PRIMARY KEY,
          name TEXT NOT NULL,
          department TEXT NOT NULL
      )
  ''')
    connection.commit()
    connection.close()
