col = int(input("Enter column: "))
row = int(input("Enter row: "))

for y in range(row):
    for x in range(col):
        if (x + y) % 2 == 0:
            print("*", end="")
        if (x + y) % 2 == 1:
            print("x", end="")
    print()
