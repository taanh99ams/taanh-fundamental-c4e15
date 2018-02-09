#FUNCTIONNNNNNNNNNNNNNN

def eval(x, y, op):
    result = 0

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    return result

# x = int(input("x = "))
# y = int(input("y = "))
# op = input("Operation = ")
#
# result = eval(x, y, op)
# print("{0} {1} {2} = {3}".format(x, op, y, result))

#DEF: name of function
#Function parameters: tham so dau vao
