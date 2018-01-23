print("Hi there, this is superuser gateway")

n = 0
while n < 3:
    name = input("Username: ")
    pw = input("Password: ")
    if name == "c4e":
        if pw == "123":
            print("Welcome")
            break
        else:
            print("Your password is wrong")
    else:
        print("You are not superuser")
    n += 1
print("Get away!")
