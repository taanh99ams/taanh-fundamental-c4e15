column = int(input("How many stars on each row? "))
row = int(input("How many rows? "))

for i in range(row):
    for i in range(column):
        print("*", end="")
    print()
