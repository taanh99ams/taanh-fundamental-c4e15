# person = ["Tuan Anh", 22, 2, "Hanoi", "Moc Chau", 5, "Maria", "Ping Pong"]: list co nhieu loai => khong phu hop dung list

# DICTIONARY

# person = {}                              dictionary rong
# print(person)
#
# person = {                              dictionary with 1 phan tu
#     #key  : value
#     "name": "Tuan Anh"
#
# }
#
# print(person)

person = {
    "name": "Tuan Anh",
    "age": 22,
    "sex": "male"
}

# READ#
# # print(person)
# # print( person["name"] )          #=> Tuan Anh
#
# if "age" in person:
#     print( person["age"] )


# 3 VONG FOR
# for key in person:
#     print(key, person[key])
#
# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)


# UPDATE
# person["age"] = 23
# person["age"] += 1
# print(person)

# person["project"] = 5
# print(person)

# DELETE
# del person["age"]
# print(person)
