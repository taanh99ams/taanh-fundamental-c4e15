print("Hi there")
print("*" * 30)
favs = ["death note", "netflix", "teaching"]
print(* favs, sep=" ")
print("*" * 30)

# i = 1
# for fav in favs:
#     print(i , end=" ")
#     print(fav)
#     i = i + 1

# for (i, v) in enumerate(favs):             # A BETTER WAY
#     print(i + 1, v)
#
# print("*" * 30)

# i = 1
# for fav in favs:
#     print("{0}. {1}".format(i, fav))
#     i += 1

for index, fav in enumerate(favs):
    # print(index  fav)
    s = "{0}. {1}".format(index + 1, fav)
    print(s)
