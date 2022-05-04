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

# Indents to keep form in viewport when writing a new journal entry.
INPUT_INDENT_RIGHT = 33
INPUT_INDENT_BOTTOM = 130

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
        tag="Entry Text",
        multiline=True,
        width=WINDOW_WIDTH - INPUT_INDENT_RIGHT,
        height=WINDOW_HEIGHT - INPUT_INDENT_BOTTOM
    )
    # TODO: Only enable SUBMIT when text exists in the input form.
    dpg.add_button(label="SUBMIT", callback=submit_entry)
    dpg.add_button(label="CANCEL", callback=cancel_entry)


# Handles callback when 'Cancel' button is pressed when creating a new entry.
def cancel_entry():
    """
    cancel_entry

    Closes the form for creating a new journal entry.
    """
    dpg.pop_container_stack()
    dpg.delete_item("Entry Form")


# Handles callback when 'Submit' button is pressed when creating a new entry.
def submit_entry():
    """
    submit_entry

    Saves a new journal entry to the database and then closes the form for
    creating a new journal entry.
    """
    # TODO: Encrypt entry.
    aes.aes_round_keys("aaaaaaaaaaaaaaaa")
    aes.aes_round_keys("abababababababab")
    aes.aes_round_keys("zzzzzzzzzzzzzzzz")
    aes.aes_round_keys("abcabcabcabcabca")
    aes.aes_round_keys("1234567890987654")
    aes.aes_round_keys("a1b2c3d4e5f6g7h8")

    # Store entry to database.
    database.submit_entry(dpg.get_value("Entry Text"))

    # Add new button to UI.
    database.display_newest()

    # Tell the GUI that this window is no longer in focus.
    dpg.pop_container_stack()

    # Delete the form for submitting a new entry.
    dpg.delete_item("Entry Form")
