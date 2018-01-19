n = int(input("Enter a number "))
digit = 0

while n > 0:    #lặp đến khi nào
    digit += 1
    n = n // 10   #n //= 10

print(digit)
