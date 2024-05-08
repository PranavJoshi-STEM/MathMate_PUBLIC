# PROJECT_DOCUMENTATION.md - MathMate

## Overview:

MathMate is made by Pranav Joshi. This project was started on 21/DECEMBER/2023. This file is divided into multiple sections:

- Overview (this section)
- Notes
- Project explanation

## Notes:

This project uses TKinter and built-in python libraries. This project is broken into 3 phases; a sketch (1), GUI creation (2) and adding in functionality (3). This entire uses the PEP-8 python guideline for improved readablity (unless otherwise stated in file description).

## Project explanation:

###  How each page is loaded
**main.py** is used to host the root window, launch each page and navigate between pages. All the files in **/pages** contains the GUI and logic for their respective pages. Each **example_page.py** is imported into **main.py** to be ran within a Tkinter frame.  When switching pages, each widget in the frame gets destroyed (deleted) from memory, thus ensuring the program does not unexpectedly crash after too many page changes.'

### How each widget is rendered
Most widgets are rendered using relative values of .place().  What that means is depending on the window size, the widgets will auto adjust to be in their proper locations.  It's important to note that the resizing of the frame is restricted due to the background image.  NO ABSOLUTE VALUES ARE USED SINCE THEY WONT WORK ON A DIFFERENT SYSTEM.

## Tests
This project was tested on Windows 11 Home, Windows 10 Education and a recent version of MacOS with no reported issues.
