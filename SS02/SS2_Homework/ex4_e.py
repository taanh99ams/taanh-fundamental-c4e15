
x = int(input("How many rows? "))
y = int(input("How many columns? "))

for u in range(x):
    if u % 2 == 0:
        if y % 2 == 0:
            for i in range(y // 2):
                print("x * ", end="")
            print()
        else:
            for i in range(y // 2):
                print("x * ", end="")
            print("x")
            print()
    else:
        if y % 2 == 0:
            for i in range(y // 2):
                print("* x ", end="")
            print()
        else:
            for i in range(y //2):
                print("* x ", end="")
            print("*")
            print()
