from datetime import datetime
import sqlite3


def setup():
    """
    setup

    Creates the entries table in the datbase if it does not already exist.
    """
    # Establish connection to database and a cursor object to manipulate it.
    connection = sqlite3.connect('./entries.db')
    cursor = connection.cursor()

    # Create the table of entries if the database doesn't yet exist.
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS
            entries (
                entryNumber integer PRIMARY KEY,
                date text,
                entry text
            )'''
    )

    for row in cursor.execute('SELECT * FROM entries ORDER BY entryNumber'):
        print(row)

    # Save (commit) the changes.
    connection.commit()

    # Close connection when finished.
    connection.close()


def submit_entry(entry_text):
    """
    submit_entry

    Saves a journal entry to the database.
    """
    # Establish connection to database and a cursor object to manipulate it.
    connection = sqlite3.connect('./entries.db')
    cursor = connection.cursor()

    # Create a new entry.
    cursor.execute(
        """
        INSERT INTO entries (
            date,
            entry
        ) VALUES (?, ?)
        """,
        (datetime.now(), entry_text)
    )

    # Save (commit) the changes.
    connection.commit()

    # Close connection when finished.
    connection.close()
