yob = int(input("Your year of birth? "))
age = 2018 - yob
print("Your age:", age)

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
elif age < 29:
    print("Preadult")
else:
    print("Adult")
