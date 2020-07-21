import random

low = 1
high = 50

numberQ = random.randint(low, high)
numberQ02 = random.randint(low, high)


question = " what is {} less than {} ".format(numberQ, numberQ02)
# print(question)

if numberQ <= numberQ02:
        print(" {} - {} =".format(numberQ02, numberQ))

else:
        print(" {} - {} =".format(numberQ, numberQ02))


