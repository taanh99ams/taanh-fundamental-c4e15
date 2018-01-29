backpack = ["xylophone", "dagger", "bedroll", "bread loaf"]

inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": backpack
}

inventory["pocket"] = ["seashell", "strange berry", "lint"]
print(inventory)

backpack.remove("dagger")
print(inventory)

inventory["gold"] += 50
print(inventory)
