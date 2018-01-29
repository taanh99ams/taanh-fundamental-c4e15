teencode = {
    "pjk": "biết",
    "ng": "người",
    "oke": "okey",
    "idk": "i don't know"
}
while True:

for key in teencode:
    print(key, end="        ")
print()

    your_code = input("Your code ")
    if your_code in teencode:
        print("Translation: ", teencode[your_code])
    else:
        print("I don't know. ", end="")
        yes_or_no = input("Do you want to create? yes or no? ")
        if yes_or_no.lower() == "yes":
            meaning = input("Meaning? ")
            teencode[your_code] = meaning
            print(*teencode)
        else:
            print("bye")

# Shift-Tab
