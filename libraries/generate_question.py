'''
Description:
    This file generates a random question based on the level and the allowed
    operations.
'''

import random

def generate_question(allowed_operations, level):
    # all possible nums that can be chosen
    num_choices = list(range(1, level*3 + 1))
    # determine type of problem
    operation = random.choice(['x', '-', '+'] + allowed_operations)

    # problem details
    details = {
        'question': '',
        'num1': 0,
        'num2': 0,
        'answer': 0,
        'operation': operation,
        # attempts is used to calculate if a hint should be given or not
        'attempts': 0,
        'completed': False, # completed is used to stop any recounting
    }

    # generate random numbers
    rand_int_1 = random.choice(num_choices)
    rand_int_2 = random.choice(num_choices)

    # all cases
    if operation=='mod':
        # make sure the first number is greater than the 2nd
        num1 = max([rand_int_1, rand_int_2])
        num2 = min([rand_int_1, rand_int_2])

        details['answer'] = num1%num2
        details['question'] = f'{num1} mod {num2}'

    elif operation=='÷':
        # make sure the answer is an integer
        answer = rand_int_2
        num2 = rand_int_1
        num1 = answer*num2

        details['answer'] = answer
        details['question'] = f'{num1} ÷ {num2}'


    elif operation=='x':
        num1, num2 = rand_int_1, rand_int_2
        details['answer'] = num1*num2
        details['question'] = f'{num1} x {num2}'

    elif operation=='+':
        num1, num2 = rand_int_1, rand_int_2
        details['answer'] = num1+num2
        details['question'] = f'{num1} + {num2}'

    elif operation=='-':
        # make sure num1 > num2 so the difference won't be negative
        num1 = max([rand_int_1, rand_int_2])
        num2 = min([rand_int_1, rand_int_2])

        details['answer'] = num1 - num2
        details['question'] = f'{num1} - {num2}'

    else:
        print('Error, how did this even happen!?')


    # write all details and return
    details['num1'] = num1
    details['num2'] = num2
    
    return details