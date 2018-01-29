print("Hello, my name is Anh and these are my sheep's sizes")
sheep = [5, 7, 300, 90, 24, 50, 75]
print(sheep)

for j in range(3):
    print("MONTH", j + 1)
    print("One month has passed. Here is my flock")
    big = max(sheep)
    # for i in range(0, len(sheep)):
    #     sheep[i] = sheep[i] + 50
    for size in sheep:
        size += 50
    print(sheep)
    print("Now my biggest sheep has", big, "Let's shear it")
    print("After shearing, here is my flock")
    sheep[sheep.index(max(sheep))] = 8
    print(sheep)






















# print()
# total = 0
# for i in range(len(sheep)):
#     x = sheep[i]
#     total += x
# print("My flock has size in total:{0}".format(total))
# money = total * 2
# print("I would get {0} * 2$ = {1}$".format(total, money))
