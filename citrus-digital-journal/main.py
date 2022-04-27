#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
"""Main.py: The entry point into the Citrus Digital Journal application."""
# ----------------------------------------------------------------------------
# author: = Christopher P. Ravosa
# course: MSCS 630L
# assignment = Final Project
# due_date: May 9, 2022
# version: 1.0
# ----------------------------------------------------------------------------

from datetime import datetime

import dearpygui.dearpygui as dpg

# Images used in task bar and decorator bar when app is running.
SMALL_ICON = "./resources/images/small-icon.ico"
LARGE_ICON = "./resources/images/large-icon.ico"

# Application viewport dimensions.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Padding to make columns clean on buttons.
PADDING = 15

# Indents to keep form in viewport when writing a new journal entry.
INPUT_INDENT_RIGHT = 33
INPUT_INDENT_BOTTOM = 130


def button_new_entry():
    # Bring new window into focus.
    dpg.push_container_stack(
        dpg.add_window(
            tag="Entry",
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
        multiline=True,
        width=WINDOW_WIDTH - INPUT_INDENT_RIGHT,
        height=WINDOW_HEIGHT - INPUT_INDENT_BOTTOM
    )
    # TODO: Only enable SUBMIT when text exists in the input form.
    dpg.add_button(label="SUBMIT", callback=button_submit_entry)
    dpg.add_button(label="CANCEL", callback=button_cancel_entry)


# Handles callback when 'Cancel' button is pressed when creating a new entry.
def button_cancel_entry():
    dpg.pop_container_stack()
    dpg.delete_item("Entry")


# Handles callback when 'Submit' button is pressed when creating a new entry.
def button_submit_entry():
    dpg.pop_container_stack()
    # TODO: Encrypt and store the entry.
    dpg.delete_item("Entry")


# TODO: Create database on first spinup.

# DPG context must be created first to access any DPG commands.
dpg.create_context()

# Instantiate a container to use as the primary window.
with dpg.window(tag="Primary Window"):
    dpg.add_text("CITRUS DIGITAL JOURNAL")
    dpg.add_text("")
    dpg.add_button(label="New Entry", callback=button_new_entry)
    dpg.add_text("")
    dpg.add_text("ENTRY NUMBER | DATE")
    # Create table to display all entries.
    with dpg.table(header_row=False):
        # Only a single column of buttons to load entries.
        dpg.add_table_column()

        # Fill rows with all entries.
        for i in range(0, 10):
            with dpg.table_row():
                entry_number_string = str(i).ljust(PADDING)
                label = entry_number_string + str(datetime.now())

                dpg.add_button(label=label)

# Create and show the window to be displayed by the OS.
dpg.create_viewport(
    title='Citrus Digital Journal',
    small_icon=SMALL_ICON,
    large_icon=LARGE_ICON,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    resizable=False
)
dpg.setup_dearpygui()
dpg.show_viewport()

# Set a primary window which fills the viewport and is always drawn first.
dpg.set_primary_window("Primary Window", True)

# Start render loop.
dpg.start_dearpygui()

# Terminate DPG.
dpg.destroy_context()
