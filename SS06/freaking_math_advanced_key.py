from random import randint, choice
from calculator_function import eval


x = randint(0, 10)
y = randint (0, 10)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)

display_result = eval(x, y, op) + error

print("{0} {1} {2} = {3}".format(x, op, y, display_result))

ans = input("Y/N? ").upper()

if error == 0:
    if ans == "Y":
        print("Bingo!")
    else:
        print("Wrong! :()")
else:
    if ans == "Y":
        print("Wrong! :()")
    else:
        print("Bingo!")
