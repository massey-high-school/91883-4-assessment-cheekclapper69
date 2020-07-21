# number check function

import random

def intcheck(question, low=1, high=100):

    # Error messages...
    if low is not None and high is not None:
            error = "please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please enter an integer that is less than or " \

    else:
        error = "please enter an integer"

    # Check that number is valid...
    while True:

        try:
            response = int(input(question))

            if low is not None and response < low:
                print(error)
                continue

            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# main routine


num_questions = intcheck("How many questions should I ask? ", 1)
low = 1
high = 50

questions_played = 0


while questions_played <= num_questions  -1:
    print()
    print("Question # {}".format(questions_played + 1))
    numbers = random.randrange(low, high)


    numberQ = random.randint(low, high)
    numberQ02 = random.randint(low, high)


    question = " what is {} less than {} ".format(numberQ, numberQ02)
    questions_played += 1
    # print(question)


    if numberQ <= numberQ02:
        print(" {} - {} =".format(numberQ02, numberQ))

    else:
        print(" {} - {} =".format(numberQ, numberQ02))