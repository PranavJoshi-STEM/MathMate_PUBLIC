"""
Description:
    This file was mostly used in development, however, some parts are still
    nessesary to the app to work.
"""

# import os so I can create a function that allows me to relative-import
# instead of absolute-import images
import os

# base configs
CONFIG = {
    'TK_WINDOW_NAME': 'PJ-786963 MathMate',
    'THEMES': ['light', 'dark', 'rose'], # all the available themes
    'SAVE_TEMPLATE': {
        'level': 3,
        'theme': 0,
        # if 'mod' or '÷' are in the list, those operations are enabled
        'enabled_ops': [],
        'session':{
            'is_limited': False,
            'total_questions': -1,
            'data': {
                'title':'Session',
                'total':0,
                'correct':0,
                'incorrect':0,
                'attempted':0,
            },
            'problem_list': [],
        },
        'lifetime': {
            'data': {
                'title':'Lifetime',
                'total':0,
                'correct':0,
                'incorrect':0,
                'attempted':0,
            },
        },
    },
}

# create a function that allows for relative import (so it works even if
# terminal isn't running in the directory)
def rel_proj_path(*path_dirs_and_file):
    # absolute path of config.py (this file)
    CONFIG_PY_PATH = os.path.abspath(__file__)
    # project directory
    PROJECT_DIR = os.path.dirname(os.path.dirname(CONFIG_PY_PATH))
    PATH = os.path.join(PROJECT_DIR, *path_dirs_and_file)
    return PATH