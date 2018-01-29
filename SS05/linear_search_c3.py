nums = [0, 7, 18, 29, 34, 46]


while True:
    num_to_find = int(input("Enter a number "))
    for index, num in enumerate(nums):
        if num == num_to_find:
            print("Found at index", index)
            break
else:
    print("Not found")
