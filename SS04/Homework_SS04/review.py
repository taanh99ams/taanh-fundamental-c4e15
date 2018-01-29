# Find sum: 0 to 2n

# x = int(input("Enter an even number"))
#
# sumx = 0
#
# for i in range(0, x + 1, 2):
#     sumx = sumx + i
#
# print("Sum =", sumx)

# from turtle import *
#
# shape("turtle")
# speed(0)
#
# for i in range(100, 400, 10):
#     forward(i)
#     left(90)
# j = 1
# while j <= 3:
#     j += 1
#     n = int(input("Enter a number bigger than 0 "))
#
#     product = 1
#
#     for i in range(1, n + 1):
#         product = product * i
#
#     print("Factorial of n =", product)
#
# row = int(input("Enter the number of row "))
# col = int(input("Enter the number of column "))
#
# for j in range(row):
#     for i in range(col):
#         if (i + j) % 2 == 0:
#             print("*", end="")
#         else:
#             print("x", end="")
#     print()

# from turtle import *
# shape("turtle")
# speed(0)
#
# for i in range(4):
#     left(30)
#     forward(50)
#     right(60)
#     forward(50)
#     right(120)
#     forward(50)
#     right(60)
#     forward(50)
#     right(60)
#
#
#
#
#
#
#
# mainloop()



# from random import randint
#
# count = 1
# while count <= 3:
#     num = randint(0, 100)
#     print("The random num is", num)
#     count += 1
#

# from random import randint
# x = randint(0, 100)
# print(x)
#
# count = 1
# while count <= 5:
#     guess = int(input("Guess the key number "))
#     if guess < x:
#         print("Too small")
#     elif guess > x:
#         print("Too big")
#     else:
#         print("Bingo! You're so smart")
#         break
#     count += 1
#
# num = int(input("Enter a number "))
#
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
#
# print("Number of digits",count)

# count = 0
# while count <= 10:
#     num = int(input("Enter a number "))
#     for i in range(2, num):
#         if num % i == 0:
#             print("No")
#             break
#         i += 1
#     else:
#         print("Yes")
#     count += 1

# menu = ["Bread","Juice","Tea","Noodle","Banh mi"]
#
# # Create:
#
# menu.append("Banana")
# print(*menu, sep=", ")
#
# for index, food in enumerate(menu):
#     print("{0}. {1}".format(index + 1, food))
