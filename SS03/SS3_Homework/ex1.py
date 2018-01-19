num = int(input("Enter a number "))

if num <= 1:
    print(num, "is not prime number")
elif num == 2:
    print(num, "is a prime number")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "is not prime number")
            break
        else:
            print(num, "is prime number")
            break
        i += 1
