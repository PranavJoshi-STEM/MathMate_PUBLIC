"""
Description:
    This file has functions that are related to saving files.
    These functions are needed to save data so session data can be saved
    between programs runs.
"""

# import configs
from configs.config import rel_proj_path, CONFIG

# import json to deal with loading and saving dictionaries
import json
FILENAME = 'mathmate_save.txt'

# save data
def save(contents, filename=FILENAME):
    PATH = rel_proj_path(filename)
    with open(PATH, 'w') as f:
        f.write(json.dumps(contents))


# return data from file
def load(filename=FILENAME):
    try:
        PATH = rel_proj_path(filename)
        with open(PATH) as f:
            contents = json.loads(f.read())
        return contents
    # return nothing if the file doesn't exist or is unreadable
    except (FileNotFoundError, json.JSONDecodeError):
        return None


# load data from a file when the program first starts
# (make sure there are no errors)
def on_start_read():
    saved_data = load()
    path = rel_proj_path('/')
    # if the file isn't valid
    if saved_data is None:
        save(CONFIG['SAVE_TEMPLATE'])
        print(f'New file created at {path}.')
        return CONFIG['SAVE_TEMPLATE']
    else:
        print(f'Loaded data:\n\n{saved_data}')
        return saved_data