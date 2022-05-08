#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
"""Database.py: Handles data updates & queries for Citrus Digital Journal."""
# ----------------------------------------------------------------------------
# author: = Christopher P. Ravosa
# course: MSCS 630L
# assignment = Final Project
# due_date: May 9, 2022
# version: 1.0
# ----------------------------------------------------------------------------

from datetime import datetime
import sqlite3
import dearpygui.dearpygui as dpg
import callbacks

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
            )
        '''
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

    # Query the database for every journal entry and make buttons for them.
    for row in cursor.execute('SELECT * FROM entries ORDER BY entryNumber'):
        entry_number = str(row[0])
        entry_number_string = entry_number.ljust(PADDING)
        label = entry_number_string + row[1]
        dpg.add_button(
            label=label,
            callback=lambda s, a, u:
                callbacks.display_entry(u),
            user_data=entry_number
        )

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

    # Query database for last entry and create a button for it.
    for row in cursor.execute(
            'SELECT * FROM entries ORDER BY entryNumber DESC LIMIT 1'
    ):
        entry_number = str(row[0])
        entry_number_string = entry_number.ljust(PADDING)
        label = entry_number_string + row[1]
        dpg.add_button(
            label=label,
            parent="Primary Window",
            callback=lambda s, a, u:
                callbacks.display_entry(u),
            user_data=entry_number
        )

    # Close connection when finished.
    connection.close()


def get_entry_text(entry_number):
    """
    get_entry_text

    Retrieves the encrypted text associated with an entry in the database.
    """
    # Establish connection to database and a cursor object to manipulate it.
    connection = sqlite3.connect('./entries.db')
    cursor = connection.cursor()

    # Query the database for a specific journal entry and get its content.
    for row in cursor.execute(
            'SELECT * FROM entries WHERE entryNumber = ?',
            [entry_number]
    ):
        entry_text = str(row[2])

    # Close connection when finished.
    connection.close()

    # Send back the encrypted entry.
    return entry_text
