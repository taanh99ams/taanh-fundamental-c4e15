nums = [1, 15, 37, 38, 57, 96]

num_to_find = int(input("Enter a number "))

#1. Assumption
found_index = -1  #Not found

#2 Create a loop to test our Assumption
for index, num in enumerate(nums):
    if num == num_to_find:
         found_index = index #Update Assumption
         break


if found_index == -1:         #If beginning assumption still true, then num is not in the list
    print("Not found")
else:
    print("Found at index", found_index)
