while True:
    num = int(input("Enter a number? "))
    if num <= 1:
        print(num, "is not a prime number")
    elif num == 2:
        print(num, "is a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
