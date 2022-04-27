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
import database
import callbacks

# Images used in task bar and decorator bar when app is running.
SMALL_ICON = "./resources/images/small-icon.ico"
LARGE_ICON = "./resources/images/large-icon.ico"

# Application viewport dimensions.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Padding to make columns clean on buttons.
PADDING = 15

# Establish connection to database.
database.setup()

# DPG context must be created first to access any DPG commands.
dpg.create_context()

# Instantiate a container to use as the primary window.
with dpg.window(tag="Primary Window"):
    dpg.add_text("CITRUS DIGITAL JOURNAL")
    dpg.add_text("")
    dpg.add_button(label="New Entry", callback=callbacks.new_entry)
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

# TODO: Ability to click on an entry to view encrypted version. Decrypt button with prompt for key.
