# x = int(input("Enter a number: "))
#
# print("Sum =", x*(x+1)/2)

# x = int(input("Enter a number: "))
# print("Sum =" sum(range(0, x))

x = int(input("Enter a number: "))

total = 0

for i in range(x + 1):
    total += i
    print(i)

print(total)
