x = int(input("Enter a number "))

if x % 2 == 0:
    for i in range(x // 2):
        print("x * ", end="")
    print()
else:
    for i in range(x // 2):
        print("x * ", end="")
    print("x")
