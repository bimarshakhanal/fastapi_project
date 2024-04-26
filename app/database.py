'''Create data base connection and create required tables'''
import logging
import sqlite3

logging.basicConfig(filename='app.log')
DATABASE_URI = "data.db"


def create_connection():
    """Connects to the SQLite database and returns a connection object."""
    try:
        connection = sqlite3.connect(DATABASE_URI)
        return connection
    except ConnectionError:
        logging.error('Failed to connect to database')


def create_table(connection):
    """
    Creates the 'employees' table in the database based on the Employee model.
    """
    try:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    ''')
        connection.commit()
    except sqlite3.OperationalError:
        logging.error('Failed to create table')

    # connection.close()
