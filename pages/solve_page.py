"""
Description:
    This file contains the GUI structure of the solve page.
"""

# import tkinter
from tkinter import *

# for the progress bar
from tkinter.ttk import Progressbar
from tkinter import ttk

# import configs
from configs.all_themes import ALL_THEMES, get_theme
from configs.config import rel_proj_path

# import components
from components.header import add_header_GUI

# import libraries
from libraries.generate_hint import generate_hint
from libraries.generate_question import generate_question
from libraries.handle_saving import save


# page GUI
def solve_page(root_win, nav_func, all_details):
    global problem_count

    # --- FUNCTIONS THAT RUN ON BUTTON PRESS ---
    def prev_btn_press():
        global problem_count
        # can't go to any previous questions
        if problem_count==0:
            prev_btn.configure(state='disabled')
        else:
            # disable the button if the next problem is going to be the first
            if problem_count==1:
                prev_btn.configure(state='disabled')
            # enable the next button if it's disabled
            next_btn.configure(state='normal')
            # track everything
            problem_count-=1
            problem = all_details['session']['problem_list']
            equation.set(problem[problem_count]['question'])
            # enable the submit button if the question is solvable
            if not problem[problem_count]['completed']:
                submit_btn.configure(state='normal')
            # indicate if the problem is solvable or not
            indicate(problem, problem_count)




    def next_btn_press(from_submit_button = False):
        global problem_count

        # enable the submit_btn (unless otherwise)
        submit_btn.configure(state='normal')

        # generate next question
        all_details['session']['problem_list'].append(
            generate_question(
                all_details['enabled_ops'],
                all_details['level']
            )
        )

        # if the problem is already solved, disable the submit_btn
        # (unless this is the 1st question)
        if (all_details['session']['problem_list']
            [problem_count+1]['completed']):
            submit_btn.configure(state='disabled')

        # if the problem is unsolved, remove messages
        if all_details['session']['problem_list'][
            problem_count
            ]['completed']==False:
            update_icons_and_response(resp=2)


        # keep track of everything
        problem_count+=1
        print(problem_count) # debugging
        # enable the prev_btn since you can go to the previous question now
        prev_btn.configure(state='normal')
        # don't state attempts if question is right/wrong
        if not from_submit_button:
            indicate(all_details['session']['problem_list'], problem_count)
        equation.set(all_details['session']['problem_list']
                     [problem_count]['question'])
        hint_text.set('') # clear hints
        # update stats GUI
        all_details['session']['data']['total']+=1
        all_details['lifetime']['data']['total']+=1
        session_text.set(format_stats(all_details['session']['data']))
        lifetime_text.set(format_stats(all_details['lifetime']['data']))

        # keep track of everything unique to limited sessions
        if limited_session:
            if from_submit_button: # only increase value if solved
                answered.set(answered.get()+1)
            count_str.set(f"""{answered.get()}/{
                                all_details['session']['total_questions']
                            } questions done""") 
        
        # save all data
        save(all_details)



    def submit_btn_press(from_keypress=False):
        # if the button is disabled, don't do anything
        if from_keypress and submit_btn['state']=='disabled':
            print('User tried to submit but button was disabled!')
            # exit out of function without doing anything
            return 'exit out of function without doing anything'
        # the math problem
        problem = all_details['session']['problem_list'][problem_count]
        response = input_entry.get() # the user's answer

        # make sure the problem isn't completed
        if problem['completed']==False:
            # make sure it is an integer
            try:
                response = int(response)
                # if the user got it correct
                if response==problem['answer']:
                    print('User got it correct!')
                    all_details['session']['problem_list'][
                        problem_count]['completed']=True
                    # display checkmark icon and correct answer
                    update_icons_and_response(1, answer=response)
                    # update stats
                    all_details['session']['data']['correct']+=1
                    all_details['session']['data']['attempted']+=1
                    all_details['lifetime']['data']['correct']+=1
                    all_details['lifetime']['data']['attempted']+=1
                    next_btn_press(from_submit_button=True) # next question

                # user got it wrong
                else:
                    # user took too many attempts
                    if problem['attempts']==3:
                        all_details['session'][
                            'problem_list'][problem_count]['completed']=True
                        # update stats
                        all_details['session']['data']['incorrect']+=1
                        all_details['session']['data']['attempted']+=1
                        all_details['lifetime']['data']['incorrect']+=1
                        all_details['lifetime']['data']['attempted']+=1
                        # feedback
                        answer = problem['answer']
                        update_icons_and_response(0,
                                                  CUSTOM_MSG=f'Failed. \
It was {answer}') # wrong
                        
                        next_btn_press(from_submit_button=True) #next question

                    # user still has a few tries
                    else:
                        problem['attempts']+=1
                        all_details['session'][
                            'problem_list'][
                                problem_count]['attempts']=problem['attempts']
                        # incorrect response
                        update_icons_and_response(0,
                                            attempts=problem['attempts'])

                    # write hint when applicable
                    problem = all_details['session'][
                        'problem_list'][problem_count]
                    hint_text.set(generate_hint(
                        problem['operation'], problem['attempts'],
                        problem['num1'], problem['num2']))
                    
            except:
                update_icons_and_response(-1) # invalid response
                print('User submitted in-valid response:', response)
        else:
            update_icons_and_response(2) # clear message

        # clear the entry
        input_entry.delete(0, END)


    

    # --- OTHER FUNCTIONS ---
    # on button press, I can re-render this
    def update_icons_and_response(resp, attempts=0, answer=0, CUSTOM_MSG=''):
        # 0=wrong, 1=right, 2=clear, -1=what???
        TYPE_OF_RESPONSE = ['wrong', 'correct', 'question'][resp]
            # icon
        if resp!=2: # no messages/icons should be displayed when resp==2
            icon = PhotoImage(file=rel_proj_path('assets',
                                        PALLETE[f'icon-{TYPE_OF_RESPONSE}']))
            # make the image half the size of the original
            icon = icon.subsample(2, 2)
            icon_label = Label(resp_frame, image=icon, bg=PALLETE['bg'])
            icon_label.image = icon # stop Python's garbage collecter
        elif resp==2:
            icon_label = Label(resp_frame, bg=PALLETE['bg'])
        # forget old icon_label if already placed to stop overlapping
        try:
            icon_label.place_forget()
        except:
            pass # do nothing as intended
        icon_label.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)
        MSG = [f'Incorrect, {4-attempts} attempts left!', 
                f'Correct, it was {answer}!', '','Please enter a valid number!'
              ][resp]
        # override msg if wanted
        if CUSTOM_MSG!='':
            MSG=CUSTOM_MSG
        response = Label(resp_frame, text=MSG, bg=PALLETE['bg'],
                         fg=PALLETE[f'resp-{TYPE_OF_RESPONSE}'])
        # forget old response if already placed to stop overlapping
        try:
            response.place_forget()
        except:
            pass # do nothing as intended
        response.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.4)


    # indicate the attempts on the question
    # 0=wrong, 1=correct, 2=clear msgs, -1=what???
    def indicate(problem_list, problem_count):
        # show how many attempts are left if the question is incomplete
        if (problem_list[problem_count]['completed']==False):
            print(problem_count, len(problem_list)+1) # debugging
            submit_btn.configure(state='normal')
            update_icons_and_response(2,
                CUSTOM_MSG=f'You have {4-problem["attempts"]} attempts left.')
        else:
            update_icons_and_response(-1, 
                CUSTOM_MSG='You have already attempted this\n problem \
and cannot attempt it again.')
            submit_btn.configure(state='disabled')


    # format the stats so it can be displayed on the screen
    def format_stats(data):
        # extract data because I can't directly access the values in the
        # F-string for some reason :O
        [title, total, correct, incorrect, attempted] = list(data.values())

        text = f'{title}:\n'
        text += ('-'*len(title)) + '\n' # underline title
        text += f'Total: {total}\n'
        text += f'Correct: {correct}\n'
        text += f'Incorrect: {incorrect}\n'
        text += f'Attempted: {attempted}'

        return text


    # --- ON PAGE LOAD ---
    # generate a question if the problem_list is empty
    if len(all_details['session']['problem_list'])==0:
        generated_question = generate_question(all_details['enabled_ops'],
                                            all_details['level'])
        all_details['session']['problem_list'].append(generated_question)
    # keep track of the problem number
    problem_count = len(all_details['session']['problem_list'])-1


    # --- TKINTER VARIABLES ---
    # load details
    limited_session = all_details['session']['is_limited']
    if limited_session:
        answered = IntVar(value=all_details['session']['data']['attempted'])
        questions = all_details['session']['total_questions']
        # counter next to progress bar
        count_str = StringVar(
            value=f'{answered.get()}/{questions} questions done')

    # equation in flashcard
    equation = StringVar(value=all_details['session']
                         ['problem_list'][problem_count]['question'])

    # the hint
    hint_text = StringVar()
    problem = all_details['session']['problem_list'][problem_count]
    hint_text.set(generate_hint(problem['operation'], problem['attempts'],
                              problem['num1'], problem['num2']))

    # the text displayed to the user
    session_text = StringVar(value=format_stats(
        all_details['session']['data']))
    lifetime_text = StringVar(value=format_stats(
        all_details['lifetime']['data']))


    # --- SETUP ---
    # create a page
    page = Frame(root_win)
    # get theme and pallete
    THEME, PALLETE = get_theme(all_details)
    # set background colour
    page.configure(bg=PALLETE['bg'])
    # set background image
    BG_IMG = PhotoImage(file=rel_proj_path('assets', PALLETE['bg-img']))
    BACKGROUND = Label(page, image=BG_IMG)
    BACKGROUND.image = BG_IMG # stop Python's garbage collecter
    BACKGROUND.grid(row=0, column=0, rowspan=10, sticky=NSEW)
    # navigators
    to_settings_page = lambda:nav_func(root_win, 'settings_page', all_details)
    # header
    header_frame = Frame(page)
    add_header_GUI(header_frame, PALLETE, 'Settings', to_settings_page)


    # --- UNIQUE PAGE GUI ---
    # Progress bar (only render progress bar if needed)
    if limited_session:
        progbar_frame = Frame(page, width=1024, height=15)
            # create style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TProgressbar', thickness=30, troughcolor='gray',
                        background=PALLETE['progress-bar'],
                        troughrelief='flat')
            # make bar
        bar = Progressbar(progbar_frame, length=830, mode='determinate',
                          maximum=questions, variable=answered,
                          style='TProgressbar')
            # make a label
        count = Label(progbar_frame, textvariable=count_str,
                      fg=PALLETE['text'], bg=PALLETE['bg'])
            # place frames
        bar.grid(row=0, column=0, sticky=NSEW)
        count.grid(row=0, column=1, sticky=NSEW)

        progbar_frame.place(relx=0.02, rely=0.08, relwidth=0.96)
    

    # Flashcard and buttons    
        # flashcard
    flashcard_btns_frame = Frame(page, width=1024, height=200, bd=5,
                                 bg=PALLETE['flashcard-border'])
    flashcard = Label(flashcard_btns_frame, textvariable=equation,
                      fg=PALLETE['text'], bg=PALLETE['bg'],
                      font=PALLETE['flashcard-font'])
        # buttons
    prev_btn = Button(flashcard_btns_frame, text='Previous', width=10,
                      padx=10, pady=10, command=prev_btn_press)
    if problem_count==0: # disable the button if it's the first question
        prev_btn.configure(state='disabled')
    next_btn = Button(flashcard_btns_frame, text='Next', width=10, padx=10,
                      pady=10, command=next_btn_press)
        # place frames
    flashcard.place(relx=0, rely=0, relwidth=1, relheight=0.7)
    prev_btn.place(relx=0, rely=0.7, relwidth=0.5, relheight=0.3)
    next_btn.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.3)

    flashcard_btns_frame.place(relx=0.08, rely=0.2, relwidth=0.37,
                               relheight=0.27)


    # Input field, response and hint frame
        # input field
    input_frame = Frame(page, bg=PALLETE['bg'])
    input_label = Label(input_frame, bg=PALLETE['bg'], fg=PALLETE['text'],
                        text='Write your answer here!')
    input_field = Frame(input_frame, bg=PALLETE['text'])
    input_entry = Entry(input_field, text='Enter a valid number here!',
          fg=PALLETE['entry-field'])
        # bind the enter key with input_entry
    input_entry.bind('<Return>', lambda unused: submit_btn_press(from_keypress=True))
    input_entry.grid(sticky=NSEW)
    submit_btn = Button(input_frame, text='Submit', command=submit_btn_press,
                        fg='black', height=2, width=10)
        # place the widgets inside the input field
    input_label.place(relx=0.18, rely=0.09)
    input_field.place(relx=0.18, rely=0.18)
    submit_btn.place(relx=0.63, rely=0.1)
        # response frame (has icon and response text)
    resp_frame = Frame(input_frame, bg=PALLETE['bg'])
    update_icons_and_response(2)
    
        # hint
    hint = Label(input_frame, fg=PALLETE['hint'], bg=PALLETE['hint-bg'],
                 textvariable=hint_text)
        # place frames
    input_frame.place(relx=0.5, rely=0.2, relwidth=0.45, relheight=0.3)
    resp_frame.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.3)
    hint.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.25)


    # Stats
        # session data
    session_stats = Label(page, textvariable=session_text,
                          fg=PALLETE['text'], bg=PALLETE['bg'],
                          font=PALLETE['stats-font'])
    session_stats.place(relx=0, rely=0.55, relwidth=0.25, relheight=0.25)
        # lifetime data
    lifetime_stats = Label(page, textvariable=lifetime_text,
                           fg=PALLETE['text'], bg=PALLETE['bg'],
                           font=PALLETE['stats-font'])
    lifetime_stats.place(relx=0.75, rely=0.55, relwidth=0.25, relheight=0.25)


    # render and return the GUI
    page.pack()
    return page