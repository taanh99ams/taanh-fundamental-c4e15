print("Guess your number game")
print("Now think of a number ranged from 1 to 100")
print("All you have to do is answer my guess")
print("c is correct")
print("s is smaller")
print("l is larger")

# print('''
# Hi there,
# Now think of
# ''')

lo = 0
hi = 100
loop = True
while loop:
    mid = (lo + hi) // 2
    answer = input("Is " + str(mid) + " your answer?")
    if answer.lower() == "c":
        print("I knew it")
        loop = False
    elif answer.lower() == "s":
        hi = mid
    elif answer.lower() == "l":
        lo = mid









               #.lower chuyen ve chu lower
