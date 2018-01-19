# from random import randint
#
# x = randint(1, 100)
# print(x)
#
# count = 0
# while True:
#     y = int(input("Guess a number: "))
#     if y < x:
#         print("Too small")
#     elif y = x:
#         print("Bingo")
#     else:
#         print("Too big")
#     count += 1
#     if count = x:
#         break

from random import randint

x = randint(1, 100)
print(x)
loop = True

count = 0
while loop:

    y = int(input("Guess a number: "))

    if y < x:
        print("Too small")
    elif y = x:
        print("Bingo")
        loop = False
    else:
        print("Too big")
    count += 1
