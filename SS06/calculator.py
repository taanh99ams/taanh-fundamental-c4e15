x = int(input("Enter x "))
op = input("Operation (+, -, *, /) ")
y = int(input("Enter y "))

op_list = ["+", "-", "*", "/"]
#
# print("*" * 20)
# if operation == "+":
#     print("{0} + {1} = {2}".format(x, y, x + y))
# elif operation == "-":
#     print("{0} - {1} = {2}".format(x, y, x - y))
# elif operation == "*":
#     print("{0} * {1} = {2}".format(x, y, x * y))
# elif operation == "/":
#     print("{0} / {1} = {2}".formay(x, y, x / y))
# else:
#     print("Wrong operation")
#
# print("*" * 20)

# Better way
result = 0
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y
else:
    print("Unsupported operation")

print("{0} {1} {2} = {3}".format(x, op, y, result))
