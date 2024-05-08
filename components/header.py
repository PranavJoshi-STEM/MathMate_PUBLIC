"""
Description:
    This file contains all the GUI for the header used on the solve and
    settings page.
"""

from tkinter import *
from random import choice

def add_header_GUI(frame, pallete, btn_text, change_page_func,
                   tag="Welcome to MathMate, we're \
going to have a great time!"):
    # put background
    frame.configure(bg=pallete['bg'])

    # pick random greeting
    greeting_text = choice(['Howdy!', 'Hello!', 'Hi :D', "What's up?",
                            'Looking sharp!', 'Smarty pants!', 'Genius-mode!',
                            'Time for math', 'Keep at it!',
                            "Whoa... you're so smart!",
                            'Good day!', 'Whoooo!', 'Math > Videogames'])
    greeting = Label(frame, text=greeting_text, height=2, width=25,
                       bg=pallete['last-saved'], fg=pallete['text'])
    greeting.pack(side='left', padx=1)

    # app name
    app_name = Label(frame, text=tag, height=2, bg=pallete['bg'],
                     fg=pallete['text'], font=pallete['title'])
    app_name.pack(side='left', padx=5)

    # button to switch pages
    button = Button(frame, text=btn_text, command=change_page_func,
                    height=2, width=15)
    button.pack(side='right', padx=3)

    # render GUI
    frame.place(relx=0, rely=0, relwidth=1, relheight=0.07)