#02_pa component


import random

low = 1
high = 100

for item in range (0, 20):
    secret = random.randint(low, high)
    print(secret, end="\t")
