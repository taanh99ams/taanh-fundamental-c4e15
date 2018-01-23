
word = "champion"

from random import shuffle
wordlist = [i for i in word]
shuffle(wordlist)
print(*wordlist)

answer = (input("Please input your guess for the word about: ")).lower()

if answer == word:
    print ("Hura")
else:
    print (":(")
