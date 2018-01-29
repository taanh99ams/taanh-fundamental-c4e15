nums = [1, 6, 8, 1, 2, 1, 5, 6]

while True:
    i = 0
    num_to_count = int(input("Enter a number? "))
    for num in nums:
        if num == num_to_count:
            i += 1
    if i == 0:
        print("Not in the list")
    else:
        print("{0} appear {1} times in my list".format(num_to_count, i))
