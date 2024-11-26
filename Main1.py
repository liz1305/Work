# print("Nothing\n will work\n unless you do")
#
# print("\"Anyone who\n \tstops\n \t\tlearning is old,\n \t\t\t\twhether at twenty or eighty")
#
# num1 = int(input("Enter 1st numbers: "))
# num2 = int(input("Enter 2nd numbers: "))
#
# sum: int = num1 + num2
# print(f"Total sum number: {sum} ")
# difference: int = num1 - num2
# print(f"Total difference numbers: {difference} ")
# product: int = num1 * num2
# print(f"Total product numbers: {product} ")
# divide: int = num1 / num2
# print(f"Total of divided numbers: {divide}")
#
#
# num3 = int(input("Enter 1st number: "))
# num4 = int(input("Enter 2nd number: "))
# num5 = 100
#
# percentage: int = num2 * num4
# percent = percentage / num5
# print(f"The percentage is: {percent}"


rocks = "\U0001FAA8"
tomatoes = "\U0001F345"
mushrooms = "\U0001F344"
strawberries = "\U0001F353"
leafy_greens = "\U0001F96C"
the_boy = "\U0001F468"
the_bug = "\U0001F41B"
print(tomatoes, strawberries, leafy_greens, mushrooms)
# 2nd Row
row2 = input(f"{the_bug}: What are you going to plant in the 2nd row?\n{the_boy}: ")
if row2 == tomatoes:
    amount = int(input(f"{the_bug}: How many do you want to plant?\n{the_boy}: "))
    if amount > 9:
        row2 = tomatoes * 9
    else:
        row2 = tomatoes * amount + "  " * (9 - amount)
else:
    row2 = rocks * 9
print()

# 3rd Row
row3 = input(f"{the_bug}: What are you going to plant in the 3rd row?\n{the_boy}: ")
if row3 == mushrooms:
    amount = int(input(f"{the_bug}: How many do you want to plant?\n{the_boy}: "))
    if amount > 9:
        row3 = mushrooms * 9
    else:
        if amount % 2 == 0:
            amount += 1

        row3 = mushrooms * amount + "  " * (9 - amount)
else:
    row3 = rocks * 9
print()

# 4th Row
row4 = input(f"{the_bug}: What are you going to plant in the 4th row?\n{the_boy}: ")
if row4 == strawberries:
    amount = int(input(f"{the_bug}: How many do you want to plant?\n{the_boy}: "))
    if amount > 9:
        row4 = strawberries * 9
    else:
        if amount % 3 != 0:
            # solution 1
            # amount += 1
            # while amount % 3 != 0:
            #     amount += 1

            # solution 2
            amount = amount + (3 - (amount % 3))

        row4 = strawberries * amount  + "  " * (9 - amount)
else:
    row4 = rocks * 9
print()

# 5th Row
row5 = input(f"{the_bug}: What are you going to plant in the 5rd row?\n{the_boy}: ")
if row5 == leafy_greens:
    amount = int(input(f"{the_bug}: How many do you want to plant?\n{the_boy}: "))
    if amount > 9:
        row5 = leafy_greens * 9
    else:
        if amount == 9:
            row5 = leafy_greens * 9
        else:
            row5 = leafy_greens * amount + the_bug + "  " * (8 - amount)
else:
    row5 = rocks * 9
print()

print("/" + "--" * 9 + "\\")
print("|" + row2 + "|")
print(f"|{row3}|")
print(f"|{row4}|")
print(f"|{row5}|")
print(f"\\{"--" * 9}/")