from random import randint
from random import choice

x = randint(0, 10)
y = randint(0, 10)
op_list = ["+", "-", "*", "/"]
op = choice(op_list)
error = randint(-1, 1)

print(x, op, y, "=", end=" ")

if op == "+":
    result = x + y

elif op == "-":
    result == x - y

elif op == "*":
    result = x * y

elif op == "/":
    result = x / y

print (result + error)
print()
ans = input("Y/N? ").upper()

if error == 0 and ans == "Y" or error != 0 and ans == "N":
    print("Yay")
else:
    print("Nay")
