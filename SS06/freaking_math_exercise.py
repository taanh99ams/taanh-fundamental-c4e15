from random import randint

x = randint(0, 10)
y = randint (0, 10)
result = x + y + randint(-1, 1)
print("{0} + {1} = {2}".format(x, y, result))

while True:
    ans = input("Y/N? ").upper()
    if result == x + y:
        if ans == "Y":
            print("Bingo!")
        else:
            print("Wrong! :()")
    else:
        if ans == "Y":
            print("Wrong! :()")
        else:
            print("Bingo!")

# if (result == x + y and ans == "Y") or (result != x + y and ans == "N"):
#     print("Yay")
# else:
#     print("Nay")
