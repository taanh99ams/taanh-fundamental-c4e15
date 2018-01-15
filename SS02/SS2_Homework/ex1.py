height = int(input("What is your height (in cm)? "))
weight = int(input("What is your weight (in kg)? "))

height_m = height * 1/100
bmi = weight / (height_m * height_m)
print("BMI =", bmi)

if bmi < 16:
    print("severely underweight")
elif bmi <= 18.5:
    print("underweight")
elif bmi <= 25:
    print("normal")
elif bmi <= 30:
    print("overweight")
else:
    print("obese")
