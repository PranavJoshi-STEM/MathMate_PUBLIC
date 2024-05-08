"""
Description:
    This file contains the GUI structure of the splash page.
"""

from tkinter import *

from configs.all_themes import ALL_THEMES, get_theme
from configs.config import CONFIG, rel_proj_path

# GUI of the splash_page
def splash_page(root_win, nav_func, all_details):
    # create a page
    page = Frame(root_win)
    THEME, PALLETE = get_theme(all_details)
    page.configure(bg=PALLETE['bg']) # get background

    # set background image
    BG_IMG = PhotoImage(file=rel_proj_path('assets', 'splash_bg.png'))

    BACKGROUND = Label(page, image=BG_IMG)
    # Store a reference to the image to prevent Python's automatic garbage
    # collection
    BACKGROUND.image = BG_IMG
    BACKGROUND.grid(row=0, column=0, rowspan=10, columnspan=10, sticky=NSEW)

    # navigator
    to_solve_page = lambda: nav_func(root_win, 'solve_page', all_details)

    # navigation button
    nav_btn = Button(page, text="Click me to start problem solving!", 
                     command=to_solve_page, width=30, height=4)
    #nav_btn.focus()
    nav_btn.grid(row=8, column=5)

    # return and render the GUI
    page.grid(sticky=NSEW)
    return page