
import random

def intcheck(question, low=0, high=100):

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
G_question = ""
how_many = questions_played
game_history = []
correct = ""
wrong = ""


while questions_played <= num_questions -1:
    print()
    print("Question # {}".format(questions_played + 1))
    numbers = random.randrange(low, high)

    numberQ = random.randint(low, high)
    # print(numberQ)
    numberQ02 = random.randint(low, high)
    # print(numberQ, numberQ02, end="\t")

    answer = (numberQ - numberQ02)
    question = " what is {} less than {} ".format(numberQ, numberQ02)
    questions_played += 1

    # print(question)

    if numberQ <= numberQ02:
        print(" {} - {} =".format(numberQ02, numberQ))
        answer = numberQ02 - numberQ

    else:
        print(" {} - {} =".format(numberQ, numberQ02))
        answer = numberQ - numberQ02

    G_question = intcheck("enter the answer here:")

    if G_question == answer:
        print("correct")
        feedback = "that is right"

    else:
        print("that is wrong")
        feedback = "that is wrong"

    round_result = "round {}: {}".format(questions_played, feedback)
    game_history.append(round_result)
print()
print("-----------------------------------")
print(" you have gotten to the end of the quiz ")
print("-----------------------------------")

print()
print("**** results ****")

for item in game_history:
    print(item)
