print("Hi there")
favs = ["Music", "Beach", "Orange"]

for index, fav in enumerate(favs):
    s = "{0}.{1}".format(index + 1, fav)
print(s)

# delete_fav = str(input("Thing you want to get rid of? "))
# favs.remove(delete_fav)
#
# for index, fav in enumerate(favs):
#     i = "{0}.{1}".format(index, fav)
#
# print(i)
