x = int(input("Enter a number "))

product = 1

for i in range(1, x + 1):
    product *= i
    print(i)

print("Factorial of x =", product)
