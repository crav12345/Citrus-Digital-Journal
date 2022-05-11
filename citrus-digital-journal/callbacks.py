#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
"""Callbacks.py: Handles UI item callbacks for Citrus Digital Journal."""
# ----------------------------------------------------------------------------
# author: = Christopher P. Ravosa
# course: MSCS 630L
# assignment = Final Project
# due_date: May 9, 2022
# version: 1.0
# ----------------------------------------------------------------------------

import dearpygui.dearpygui as dpg
import aes_cipher as aes
import database

# Indents to keep form in viewport.
INDENT_RIGHT = 33
INDENT_BOTTOM = 130

# Application viewport dimensions.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


def new_entry():
    """
    new_entry

    Displays the form for creating a new journal entry.
    """
    # Bring new window into focus.
    dpg.push_container_stack(
        dpg.add_window(
            tag="Entry Form",
            label="New Entry",
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            no_resize=True,
            no_move=True,
            no_collapse=True,
            no_title_bar=True
        )
    )

    # Populate the new window.
    dpg.add_text("NEW ENTRY")
    dpg.add_input_text(
        tag="Input Text",
        multiline=True,
        width=WINDOW_WIDTH - INDENT_RIGHT,
        height=WINDOW_HEIGHT - INDENT_BOTTOM
    )
    dpg.add_button(label="SUBMIT", callback=submit_entry)
    dpg.add_button(label="CANCEL", callback=lambda s: close_window("Entry Form"))


# Handles callback when 'Cancel' button is pressed when creating a new entry.
def close_window(window_tag):
    """
    close_window

    Closes the target window.
    """
    dpg.pop_container_stack()
    dpg.delete_item(window_tag)


# Handles callback when 'Submit' button is pressed when creating a new entry.
def submit_entry():
    """
    submit_entry

    Opens a form for entering a key with which the entry will be encrypted.
    """
    # Prompt user for a secret key.
    # Bring new window into focus.
    dpg.push_container_stack(
        dpg.add_window(
            tag="Key Form",
            label="New Key",
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            no_resize=True,
            no_move=True,
            no_collapse=True,
            no_title_bar=True
        )
    )

    # Populate the new window.
    dpg.add_text("SECRET KEY")
    dpg.add_input_text(
        tag="Key Text",
        multiline=False
    )
    dpg.add_button(label="ENCRYPT", callback=encrypt_entry)


def encrypt_entry():
    """
    encrypt_entry

    Encrypts and saves a new journal entry to the database and then closes the
    form for creating a new journal entry.
    """
    # Encrypt entry.
    encrypted_text = aes.aes_encrypt(
        dpg.get_value("Input Text"),
        dpg.get_value("Key Text")
    )

    # Store entry to database.
    database.submit_entry(encrypted_text)

    # Add new button to UI.
    database.display_newest()

    # Tell the GUI that this window is no longer in focus.
    dpg.pop_container_stack()

    # Delete the form for submitting a key.
    dpg.delete_item("Key Form")

    # Tell the GUI that entry window is no longer in focus.
    dpg.pop_container_stack()

    # Delete the form for submitting a new entry.
    dpg.delete_item("Entry Form")


def key_prompt(encrypted_text):
    """
    key_prompt

    Prompts user for key to decrypt the journal entry.
    """
    dpg.push_container_stack(
        dpg.add_window(
            tag="Key Form",
            label="New Key",
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            no_resize=True,
            no_move=True,
            no_collapse=True,
            no_title_bar=True
        )
    )

    # Populate the new window.
    dpg.add_text("SECRET KEY")
    dpg.add_input_text(
        tag="Key Text",
        multiline=False
    )
    dpg.add_button(label="DECRYPT", callback=lambda s: decrypt_entry(encrypted_text))


def decrypt_entry(encrypted_text):
    """
    decrypt_entry

    Decrypts the encrypted text, closes the key prompt window, and renders the
    decrypted text.
    """
    # Grab the key from the key prompt input.
    key = dpg.get_value("Key Text")

    # Decrypt the encrypted text with the entered key.
    decrypted_text = aes.aes_decrypt(encrypted_text, key)

    # Set the text of the entry display window to the decrypted text.
    dpg.set_value("Entry Text", decrypted_text)

    # Get rid of the key form window.
    close_window("Key Form")


def display_entry(entry_number):
    """
    display_entry

    Displays the selected journal entry.
    """
    # Bring new window into focus.
    dpg.push_container_stack(
        dpg.add_window(
            tag="Entry Display",
            label="Entry Display",
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            no_resize=True,
            no_move=True,
            no_collapse=True,
            no_title_bar=True
        )
    )

    # Get the entry's text from the database.
    encrypted_text = database.get_entry_text(entry_number)

    # Populate the new window.
    dpg.add_text("Journal Entry #" + entry_number)
    dpg.add_text(encrypted_text, wrap=WINDOW_WIDTH - INDENT_RIGHT, tag="Entry Text")
    dpg.add_button(label="DECRYPT", callback=lambda s: key_prompt(encrypted_text))
    dpg.add_button(label="EXIT", callback=lambda s: close_window("Entry Display"))
