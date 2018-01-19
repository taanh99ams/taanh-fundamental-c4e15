print("Hi there, this is a superuser gateway")

count = 0

while count < 3:
    name = input("Username: ")
    pw = input("Password: ")

    if name == "c4e":
        if pw == "123":
            print("Welcome c4e")
            break
        else:
            print("Your password is incorrect")
    else:
        print("You're not superuser")

    count += 1
