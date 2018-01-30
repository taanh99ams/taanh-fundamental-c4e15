prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
for fruit in prices:
    if fruit in stock:
        print('''
* {0}
price: {1}
stock: {2}'''.format(fruit, prices[fruit], stock[fruit]))
        money = prices[fruit] * stock[fruit]
        print("Revenue of {0}: {1}".format(fruit, money))
    total += money
print("Total revenue", total)
