list_item = ["T-shirt","Sweater", "Blouse", "Jacket"]
opt = input("Welcome to our shop. What do you want (C, R, U, D)? ")
opt = opt.upper()
if opt == "R":
    print(* list_item, sep = ", ")

elif opt == "C":
    newitem = input("Enter a new item ")
    list_item.append(newitem)
    print(*list_item, sep = ", ")

elif opt == "U":
    i = int(input("Update position? "))
    if i <= len(list_item):
        new = input("New item? ")
        list_item[i - 1] = new
        print(*list_item, sep = ", ")
    else:
        print("Your choice is out of range")
elif opt == "D":
    i = int(input("Delete position? "))
    if i <= len(list_item):
        list_item.pop(i - 1)
        print(list_item)
    else:
        print("Your choice is out of range")
else:
    print("Please choose again")
