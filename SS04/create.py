print("Hi there, here you favorite things so far")

listfav = ["music", "gta", "singing"]
print(*listfav, sep=", ")                     # * remove square brankets
print(*listfav)
fav = input("Name one thing you want to add?")

listfav.append(fav)
print(*listfav, sep=", ")           #sep = seperate
