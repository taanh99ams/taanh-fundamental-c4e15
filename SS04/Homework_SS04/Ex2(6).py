print("Hello, my name is Anh and these are my sheep's sizes")
sheep = [5, 7, 300, 90, 24, 50, 75]
print(sheep)

big = max(sheep)
print("Now my biggest sheep has", big, "Let's shear it")
print("After shearing, here is my flock")
sheep[sheep.index(max(sheep))] = 8
print(sheep)

for j in range(3):
    print("MONTH", j + 1)
    print("One month has passed. Here is my flock")
    for i in range(0, len(sheep)):
        sheep[i] = sheep[i] + 50
    print(sheep)
    if j < 2:
        big = max(sheep)
        print("Now my biggest sheep has", big, "Let's shear it")
        print("After shearing, here is my flock")
        sheep[sheep.index(max(sheep))] = 8
        print(sheep)
    else:
        sumsize = sum(sheep)
        print("My flock has size in total: ", sumsize)
        summoney = sumsize * 2
        print("I would get", sumsize, " * 2$ = ", summoney, "$" )
