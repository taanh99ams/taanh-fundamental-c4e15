from getpass import getpass

print("Hi there, this is a super gateway")
x = input("Username: ")
y = getpass("Password: ")

if x == "c4e":
    if y == "codethechange":
        print("Welcome,", x)
    else:
        print("Your password is wrong")


else:
    print("You are not superuser")
