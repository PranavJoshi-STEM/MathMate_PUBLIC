'''
Description:
    This program will generate a hint based on the operation and number of
    attempts.
Code-choice:
    This file exceeds PEP-8's 80 char per line limit to improve readability
    as each line is a str (not relevant to the program) and not code.
'''

# generate a random hint
import random

# main function to generate the hint
def generate_hint(operation_type, attempts, num1, num2):
    hint = ''
    # after 3 attempts, show hint
    if attempts >= 3:
        hint = '⚠️ HINT: ' + random.choice(hints(num1, num2)[operation_type])
        return hint
    # not enough attempts have passed
    else:
        return hint


# supporting function that generates a hint for certain operations
def hints(num1, num2):
    all_hints = {
        'x': [
            f'If you have {num1} boxes, and each box has {num2} toys,\n how many toys do you have in total?',
            f'You have {num1} groups of {num2}. How many items do you\n have altogether?',
            f'Imagine you have {num1} cookies, and each cookie has \n{num2} chocolate chips. How many chocolate chips do you\n have in total?',
        ],
        '÷': [
            f'You have {num1} candies, and you want to share them \nequally with {num2} friends. How many candies will each\n friend get?',
            f'Imagine you have {num1} apples, and you want to put them \ninto {num2} baskets. How many apples will be in each\n basket?',
            f'You have {num1} stickers, and you want to give the same\n number to each of your {num2} friends. How many stickers\n will each friend get?',
        ],
        '+': [
            f'You have {num1} crayons, and your friend gives you {num2}\n more. How many crayons do you have now?',
            f'You have {num1} red apples and {num2} green apples. How\n many apples do you have in total?',
            f'Imagine you have {num1} dinosaurs, and you get {num2} more\n dinosaurs. How many dinosaurs do you have?',
        ],
        '-': [
            f'You have {num1} cookies, and you eat {num2} of them. How\n many cookies do you have left?',
            f'You have {num1} balloons, and {num2} float away. How many\n balloons do you have now?',
            f'Imagine you have {num1} fish, and {num2} swim away. How\n many fish are left?',
        ],
        'mod': [
            f"If you have {num1} toys and you want to put them in boxes\n of {num2}, what is the remainder (what's left over)?",
            f'Imagine you have {num1} candies, and you want to share them\n with your {num2} friends. What is the remainder?',
            f'If you have {num1} cookies and you want to divide them into\n plates with {num2} cookies each, what is the\n leftover (remainder)?',
        ],
    }
    return all_hints