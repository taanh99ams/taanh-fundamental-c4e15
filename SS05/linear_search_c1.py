nums = [7, 65, 10, 8, 15, 27, 32, 98, 67]

num_to_find = int(input("Enter a number"))

if num_to_find in nums:
    found_index = nums.index(num_to_find)
    print("Found {0} at index {1}".format(num_to_find, found_index)
else:
    print("Not found")
