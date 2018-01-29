bacteria = int(input("How many B bacteria are there? "))
time = int(input("How many mins? "))

for i in range(0, time, 2):
    bacteria = bacteria * 2
print("After {0} mins, we have {1} bacteria".format(time, bacteria))
