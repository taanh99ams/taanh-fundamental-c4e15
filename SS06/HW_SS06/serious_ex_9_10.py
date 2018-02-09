def get_even_list(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return(even_nums)

# nums = [1, 2, 4, 5, 6, 7, 8]
# even_nums = []
# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
