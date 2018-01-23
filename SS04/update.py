menu = ["A", "B", "c", "d"]
# menu[0] = "Pizza"
# menu[0] = menu[0].lower()
#
# print(menu)          #Self-modifying

# for food in menu:
#     x = food.lower()
#     print(x)

for index, item in enumerate(menu):
    menu[index] = item.lower()         #update

print(menu)
