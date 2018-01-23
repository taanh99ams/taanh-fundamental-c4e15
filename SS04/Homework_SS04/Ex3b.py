game = []
x = ["book", "pencil", "board", "eraser", "chalk"]

import random
game.append(random.choice(x).lower())

from random import shuffle
y = [i for i in game[0]]
shuffle(y)
print(*y)

answer = (input("Please input your guess for the word about: ")).lower()

if answer == game[0].lower():
    print ("True! You're so good")
else:
    print ("Wrong :(")
