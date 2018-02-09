def remove_dollar_sign(s):
    s = s.replace("$","")
    # print(s)
    return s

# money = input("Input ")
# money_without_dollars = remove_dollar_sign(money)
# print(money_without_dollars)

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
