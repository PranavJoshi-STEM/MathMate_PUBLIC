'''
PLEASE RUN THIS FILE TO RUN THE PROJECT.  ANY OTHER FILE WILL NOT RUN THE
PROJECT.

Name: Pranav Joshi (786963, ICS3U0-C, Period 3)
Date assigned: 21/DECEMBER/2023
Project name: PJ-786963_MathMate
Description:
    This project utilizes tkinter to draw things to the screen.  When run,
    MathMate will allow the user to answer questions.  It will then respond
    and clarify whether the answer is right or not.  This program runs using
    sessions and saves the data to a file.
Notes:
    - This project will create a save file
    - 1024x768 window
    - Project was first coded in MacOS and transferred onto Windows. Therefore,
      some lines of code were written to counter-act the obscurities of either
      operating system.
    - This project works by dividing each page into a function that gets
      ran when the user is on the respective page.
    - Phase 2 was completed on 30/DECEMBER/2023.
Code-choices:
    This entire project uses a file structure similar to real-world projects
    in development teams.  Additionally, everything is coded in PEP-8 and has
    comments (when necessary) for improved code readability.
'''

# Import statements
from tkinter import *

# Import configs
from configs.config import CONFIG
from configs.all_themes import ALL_THEMES

# Import pages
from pages.splash_page import splash_page
from pages.solve_page import solve_page
from pages.settings_page import settings_page

# Import libraries
from libraries.handle_saving import on_start_read, save


# Functions
# Navigate to another page
def navigate(container, target_page_str, all_details):
    # get background before deletion
    bg_colour = container.cget('bg')

    # Destroy current page
    for widget in container.winfo_children():
        widget.destroy()

    # restore background
    container.configure(bg=bg_colour)

    # save data
    save(all_details)

    # Based on the page you want to go to, run the correct function
    if target_page_str == 'solve_page':
        solve_page(container, navigate, all_details)

    elif target_page_str == 'settings_page':
        settings_page(container, navigate, all_details)


# Main function
def main():
    # Read any preexisting data (or create a save if the save isn't valid)
    all_details = on_start_read()

    # Create base window
    win = Tk()
    win.title(CONFIG['TK_WINDOW_NAME'])
    win.geometry('1024x768')
    win.resizable(width=False, height=False)

    # set background colour
    THEME = ALL_THEMES[CONFIG['THEMES'][all_details['theme']]]
    win.configure(bg=THEME['bg'])

    # create a deletable container
    container = Frame(win)
    container.configure(bg=THEME['bg'])
    container.grid(sticky=NSEW)

    # Start with the splash page, then navigate to other pages
    splash_page(container, navigate, all_details)

    win.mainloop()


# Entry point of script
if __name__ == '__main__':
    main()