


def intcheck(question, low, high):
    valid = False
    error = "Please enter an number between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


def statement_gen(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

statement_gen("Hello World", "&")
