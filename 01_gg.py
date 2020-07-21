how_many = 5
won = 0
lost = 0

game_history = []

print()
print(" this is a game ")
print(" type won to win and nothing to lose ")
print()

for item in range(1, how_many + 1):

    result = input("game result? ")

    if result == "won":
        feedback = "you won"
        won += 1
    else:
        feedback = "sorry, you lost"
        lost += 1

    round_result = "round {}: {}".format(item, feedback)
    game_history.append(round_result)

print()
print("**** results ****")

for item in game_history:
    print(item)
