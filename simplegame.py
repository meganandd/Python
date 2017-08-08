import random

cointoss = ["heads", "tails"]

highscores = {}

while True:
    scorecounter = 0
    username = input("Enter a username: ")
    if (username in highscores) == False:
        highscores[username] = 0
    while True:
        coin = random.randint(0, 1)
        toss = cointoss[coin]
        h_or_t = input("Heads or tails? ")
        if toss == h_or_t:
            scorecounter = scorecounter + 1
            print("You guessed correctly!")
        else:
            print("You guessed wrong!")
            print("Your score is: " + str(scorecounter))
            if scorecounter > highscores[username]:
                highscores[username] = scorecounter
            break
    for key, val in highscores.items():
        print("Player: " + key + "\tScore: " + str(val))
