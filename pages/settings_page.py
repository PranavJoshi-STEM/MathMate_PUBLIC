"""
Description:
    This file contains the GUI structure of the settings page.
"""

# import tkinter
from tkinter import *
from tkinter import ttk

# import configs
from configs.all_themes import ALL_THEMES, get_theme
from configs.config import rel_proj_path, CONFIG

# import components
from components.header import add_header_GUI

# import libraries
from libraries.generate_question import generate_question


def settings_page(root_win, nav_func, all_details):
    # --- FUNCTIONS THAT RUN ON BUTTON PRESS  ---
    def mod_checkbox_press():
        op = is_mod_on.get()
        print(op)
        # remove the operation
        if op==0:
            all_details['enabled_ops'].remove('mod')
            print(all_details['enabled_ops'])
        # add the operation
        elif op==1:
            all_details['enabled_ops'].append('mod')
            print(all_details['enabled_ops'])
        
        

    def div_checkbox_press():
        op = is_div_on.get()
        print(op)
        # remove the operation
        if op==0:
            all_details['enabled_ops'].remove('÷')
            print(all_details['enabled_ops'])
        # add the operation
        elif op==1:
            all_details['enabled_ops'].append('÷')
            print(all_details['enabled_ops'])


    # this func triggers on combobox select
    def on_difficulty_selected(event):
        # make sure its not the default text
        text = difficulty_selector.get()
        if text in level_values:
            # extract the difficulty from the string
            # by finding the number of problems (last char in string)
            # and dividing it by 4
            difficulty = int(text[-1])//3
            # if difficulty is 0, that means that is is actually 4 since
            # 12//4 = 0 ==> 12 problems is level 4
            difficulty = difficulty or 4
            # save difficulty level
            all_details['level'] = difficulty


    # makes a global change to the theme and reloads the page
    def on_theme_select():
        target_theme = theme_selection.get()
        # make sure it's not the default value
        if target_theme in list(ALL_THEMES.keys()):
            all_details['theme'] = CONFIG['THEMES'].index(target_theme)
            to_settings_page()


    # reset current session and start new with progress-bar (if applicable)
    def on_session_select():
        questions = session_selection.get()
        print(f'Input for session field: {questions}')
        # start new unlimited session
        if questions=='Unlimited':
            # start a new session and reset data
            all_details['session']['is_limited'] = False
            all_details['session']['total_questions'] = -1
            all_details['session']['problem_list'] = [
                generate_question(all_details['enabled_ops'], 
                                  all_details['level'])
            ]
            for stat in ['total', 'correct', 'incorrect', 'attempted']:
                all_details['session']['data'][stat] = 0
            # change to solve_page to alert user of the changes
            to_solve_page()
        else:
            try:
                # make sure it is valid
                questions = int(questions)
                if questions==0:
                    # cause an error so the session isn't reset
                    print(var_that_doesnt_exist)
                print(f'Creating new session with {questions} questions.')

                # start a new session and reset data
                all_details['session']['is_limited'] = True
                all_details['session']['total_questions'] = questions
                all_details['session']['problem_list'] = [
                    generate_question(all_details['enabled_ops'], 
                                      all_details['level'])
                ]
                for stat in ['total', 'correct', 'incorrect', 'attempted']:
                    all_details['session']['data'][stat] = 0
                print(all_details['session'])
                # change to solve_page to alert user of the changes
                to_solve_page()
            except:
                # don't create a new session or reset details
                pass
    

    # --- TKINTER VARIABLES ---
    # whether to include mod or div questions
    is_mod_on = IntVar(value = int('mod' in all_details['enabled_ops']))
    # selector
    is_div_on = IntVar(value = int('÷' in all_details['enabled_ops']))
    difficulty = 1
    level_selection = StringVar(value=f'Level "{difficulty}"')
    # theme (get theme and pallete)
    THEME, PALLETE = get_theme(all_details)
    theme_selection = StringVar(value=f'Choose theme: "{THEME}"')
    # session selection
    session_selection = StringVar(value='Unlimited')


    # --- SETUP ---
    # create a page
    page = Frame(root_win)
    # set background colour
    page.configure(bg=PALLETE['bg'])
    # set background image
    BG_IMG = PhotoImage(file=rel_proj_path('assets', PALLETE['bg-img']))
    BACKGROUND = Label(page, image=BG_IMG)
    BACKGROUND.image = BG_IMG # stop Python's garbage collecter
    BACKGROUND.grid(row=0, column=0, rowspan=10, sticky=NSEW)
    # navigators
    to_solve_page = lambda: nav_func(root_win, 'solve_page', all_details)
    # to_settings_page is included to refresh if the theme is changed
    to_settings_page = lambda: nav_func(root_win, 'settings_page',
                                        all_details)
    # header
    header_frame = Frame(page)
    add_header_GUI(header_frame, PALLETE, 'Start solving!', to_solve_page,
                   tag='Edit your settings')


    # --- UNIQUE PAGE GUI ---
    # Change difficulty
        # title and checkboxes
    difficulty_title = Label(page, text='Change difficulty:',
                            bg=PALLETE['bg'],
                            fg=PALLETE['text'], font=PALLETE['title'])
    mod_checkbox = Checkbutton(page, text='Enable Modulus?',
                            variable=is_mod_on,
                            height=2, width=10, command=mod_checkbox_press,
                            fg='black', bg=PALLETE['hint-bg'])
    div_checkbox = Checkbutton(page, text='Enable Divison?',
                            variable=is_div_on,
                            height=2, width=10, command=div_checkbox_press,
                            fg='black', bg=PALLETE['hint-bg'])
        # place all of it
    difficulty_title.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.1)
    mod_checkbox.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.05)
    div_checkbox.place(relx=0.05, rely=0.35, relwidth=0.2, relheight=0.05)
        # difficulty selector
    level_values = [f'Level {i}: Nums between 1-{i*3}' for i in range(1, 5)]
    difficulty_selector = ttk.Combobox(page, textvariable=level_selection,
                                       values=level_values)
    difficulty_label = Label(page, text='💡: ^open the selector to change\n \
the range of numbers', 
                            bg=PALLETE['bg'], fg=PALLETE['text'])
    difficulty_selector.configure(state='readonly')
    difficulty_selector.bind('<<ComboboxSelected>>', on_difficulty_selected)
    difficulty_selector.place(relx=0.05, rely=0.4, relwidth=0.2)
    difficulty_label.place(relx=0.05, rely=0.43, relwidth=0.2)


    # Start new session
        # title and combobox
    session_title = Label(page,
                          text='Start a new session (customise the amount \n \
of questions by entering your own number\n in the box):', bg=PALLETE['bg'],
                            fg=PALLETE['text'])
    session_selector = ttk.Combobox(page, textvariable=session_selection,
                                       values=['Unlimited', '10', '20', '30'])
    session_button = Button(page, text='Start new session', 
                            command=on_session_select)
        # place everything
    session_title.place(relx=0.35, rely=0.2, relwidth=0.25, relheight=0.1)
    session_selector.place(relx=0.35, rely=0.3, relwidth=0.25, relheight=0.04)
    session_button.place(relx=0.35, rely=0.34, relwidth=0.25)


    # Change themes
        # title
    theme_title = Label(page, text='Select a colour theme!', bg=PALLETE['bg'],
                        fg=PALLETE['text'], font=PALLETE['title'])
        # theme selector
    theme_selector = ttk.Combobox(page, textvariable=theme_selection,
                                       values=list(ALL_THEMES.keys()))
    theme_selector.configure(state='readonly')
        # button
    theme_button = Button(page, text='Apply theme', command=on_theme_select)
        # place all of it
    theme_title.place(relx=0.7, rely=0.2, relheight=0.1, relwidth=0.25)
    theme_selector.place(relx=0.7, rely=0.3, relwidth=0.25)
    theme_button.place(relx=0.7, rely=0.33, relwidth=0.25)


    # render and return the GUI
    page.pack()
    return page
