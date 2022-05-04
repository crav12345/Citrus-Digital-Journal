from datetime import datetime
import sqlite3
import dearpygui.dearpygui as dpg

# Padding to make columns clean on buttons.
PADDING = 15


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


def display_all():
    """
    display_all

    Creates button items on the UI using data from the SQLite database to
    grant users an access point to journal entries.
    """
    # Establish connection to database and a cursor object to manipulate it.
    connection = sqlite3.connect('./entries.db')
    cursor = connection.cursor()

    # Query the database for every journal entry.
    for row in cursor.execute('SELECT * FROM entries ORDER BY entryNumber'):
        entry_number_string = str(row[0]).ljust(PADDING)
        label = entry_number_string + row[1]
        dpg.add_button(label=label)

    # Close connection when finished.
    connection.close()


def display_newest():
    """
    display_newest

    Adds the newest entry's button item to the UI.
    """
    # Establish connection to database and a cursor object to manipulate it.
    connection = sqlite3.connect('./entries.db')
    cursor = connection.cursor()

    for row in cursor.execute("""SELECT * FROM entries ORDER BY entryNumber DESC LIMIT 1"""):
        entry_number_string = str(row[0]).ljust(PADDING)
        label = entry_number_string + row[1]
        dpg.add_button(label=label, parent="Primary Window")

    # Close connection when finished.
    connection.close()
