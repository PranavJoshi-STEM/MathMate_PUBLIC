"""
Description:
    All the themes used in the program.  Includes a function that returns
    the theme and colour pallete.
"""

ALL_THEMES = {
    'light': {
        'bg': 'white',
        'text': 'black',
        'bg-img': 'bg-light.png',
        'last-saved': 'cyan',
        'title': ('Verdana', 15),
        'progress-bar': 'lime',
        'flashcard-font': ('Verdana', 40),
        'flashcard-border': 'black',
        'icon-correct': 'correct_96x96.png',
        'icon-wrong': 'wrong_96x96.png',
        'icon-question': 'question_96x96.png',
        'entry-field': 'black',
        'resp-correct': 'green',
        'resp-wrong': 'red',
        'resp-question': 'black',
        'hint': 'black',
        'hint-bg': 'DarkGray',
        'stats-font': ('Verdana', 18),
    },
    'dark': {
        'bg': 'black',
        'text': 'white',
        'bg-img': 'bg-dark.png',
        'last-saved': 'blue',
        'title': ('Verdana', 15),
        'progress-bar': 'green',
        'flashcard-font': ('Verdana', 40),
        'flashcard-border': 'blue',
        'icon-correct': 'correct_96x96.png',
        'icon-wrong': 'wrong_96x96.png',
        'icon-question': 'question_96x96.png',
        'entry-field': 'black',
        'resp-correct': 'green',
        'resp-wrong': 'red',
        'resp-question': 'orange',
        'hint': 'black',
        'hint-bg': 'DarkGray',
        'stats-font': ('Verdana', 18),
    },
    'rose': {
        'bg': 'pink',
        'text': 'black',
        'bg-img': 'bg-rose.png',
        'last-saved': 'lavender blush',
        'title': ('Verdana', 15),
        'progress-bar': 'lime',
        'flashcard-font': ('Verdana', 40),
        'flashcard-border': 'blue',
        'icon-correct': 'correct_96x96.png',
        'icon-wrong': 'wrong_96x96.png',
        'icon-question': 'question_96x96.png',
        'entry-field': 'black',
        'resp-correct': 'green',
        'resp-wrong': 'red',
        'resp-question': 'black',
        'hint': 'black',
        'hint-bg': 'lavender blush',
        'stats-font': ('Verdana', 18),
    },
}

# quickly get the theme
def get_theme(all_details):
    THEME = ['light', 'dark', 'rose'][all_details['theme']]
    PALLETE = ALL_THEMES[THEME]
    return THEME, PALLETE