 # from Garden import garden_game

print("\t\t\tGarden Project\n")
rocks = "🪨"
Rocks = (f"{rocks}")
print (f"{rocks}")
tomatoes = "🍅"
Tomatoes =(f"{tomatoes}")
print (f"{tomatoes}")
mushroom = "🍄"
Mushroom = (f"{mushroom}")
print (f"{mushroom}")
strawberries = "🍓"
Strawberries = (f"{strawberries}")
print (f"{strawberries}")
leafyGreen = "🥬"
LeafyGreen = (f"{leafyGreen}")
print (f"{leafyGreen}")

plant1 = input("🐛: What are you going to plant in 2nd row?\n👦🏻: ")
tmt = int(input("🐛: How many you want to plant?\n👦🏻: "))
plant2 = input("🐛: What are you going to plant in 3rd row\n👦🏻: ")
mush = int(input("🐛: How many you want to plant?\n👦🏻: "))
plant3 = input("🐛: What are you going to plant in 4th row?\n👦🏻: ")
straw = int(input("🐛: How many you want to plant?\n👦🏻: "))
plant4 = input("🐛: What are you going to plant in last row?\n👦🏻: ")
green = int(input("🐛: How many you want to plant?\n👦🏻: "))

print("---------------------------------")

if plant1 == "🍅🍅":
     print ( "|🪨🪨🪨🪨🪨🪨🪨🪨🪨|")
elif plant1 == "🍅":
     print("|" + "🍅"*tmt +"|")


if plant2 % 2 == 0:
     print("|" + "🍄" *mush +"🍄" + "         |" )
else:
     print("|" + "🍄" *mush + "         |")

if plant3 == "🍓" and straw % 3 == 0:
     print("|" + "🍓" * straw + "        |")
else:
     print("|" + "🍓" * 9 + "|")

if plant4 == "🥬" and green <= 8:
     print("|" + "🥬" * green + "🐛" + "|")
else:
     print("|" + "🥬" * 9 + "|")
