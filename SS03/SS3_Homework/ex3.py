# 73

from random import randint

while True:
    num = randint(1, 100)
    print("Is it", num, "? ", end="")
    if num < 73:
        print("B")
    elif num == 73:
        print("C")
        break
    else:
        print("S")

print("I knew it")
