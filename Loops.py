#Task1
# start = input("Enter start number: ")
# end = input("Enter end number: ")
# for number in range(start, end + 1):
#     print(number, end = " ")

#Task2
# start = input("Enter start number: ")
# end = input("Enter end number: ")
# for number in range(start, end + 1):
#     if number % 2 != 0:
#     print(number, end = " ")

# #Task3
# start = input("Enter start number: ")
# end = input("Enter end number: ")
# while start <= end:
#     if start % 2 == 0:
#         print(start, end=" ")
#     start += 1


#Task4
# start = input("Enter start number: ")
# end = input("Enter end number: ")
# for number in range(start, end + 1):
#     print(end + 1 - number, end = " ")

#Task5
# start = input("Enter start number: ")
# end = input("Enter end number: ")
# if start > end:
#     for number in range(end, start + 1):
#         if number % 2 != ):
#             print(number, end=" ")
# else:
#     for number in range(start, end + 1):
#         if number % 2 != ):
#             print(number, end=" ")

def garden_game():
    print("🪨")
    print("🍅")
    print("🍄")
    print("🍓")
    print("🥬")
    garden_rows = {
        1: '🪨',
        2: '🍅',
        3: '🍄',
        4: '🍓',
        5: '🥬'
    }
    garden_layout = []
    garden_layout.append(garden_rows[1] * 9)

    while True:
        plant = input("🐛: What are you going to plant in the 2nd row?\n👩‍🌾: ")
        if plant == garden_rows[2]:
            num_plants = int(input("🐛: How many do you want to plant?\n👩‍🌾: "))
            num_plants = min(num_plants, 9)
            garden_layout.append(garden_rows[2] * num_plants)
            break
        else:
            print("🐛: Incorrect plant for row 2. Please plant 🍅.")

    while True:
        plant = input("🐛: What are you going to plant in the 3rd row?\n👩‍🌾: ")
        if plant == garden_rows[3]:
            num_plants = int(input("🐛: How many do you want to plant?\n👩‍🌾: "))
            num_plants = min(num_plants, 9)
            if num_plants % 2 == 0:
                num_plants += 1 if num_plants < 9 else 0
            garden_layout.append(garden_rows[3] * num_plants)
            break
        else:
            print("🐛: Incorrect plant for row 3. Please plant 🍄.")

    while True:
        plant = input("🐛: What are you going to plant in the 4th row?\n👩‍🌾: ")
        if plant == garden_rows[4]:
            num_plants = int(input("🐛: How many do you want to plant?\n👩‍🌾: "))
            num_plants = min(num_plants, 9)
            if num_plants % 3 != 0:
                num_plants += 3 - (num_plants % 3)
            garden_layout.append(garden_rows[4] * num_plants)
            break
        else:
            print("🐛: Incorrect plant for row 4. Please plant 🍓.")

    while True:
        plant = input("🐛: What are you going to plant in the 5th row?\n👩‍🌾: ")
        if plant == garden_rows[5]:
            num_plants = int(input("🐛: How many do you want to plant?\n👩‍🌾: "))
            num_plants = min(num_plants, 9)
            row_str = garden_rows[5] * num_plants
            if num_plants <= 8:
                row_str += '🐛'
            garden_layout.append(row_str)
            break
        else:
            print("🐛: Incorrect plant for row 5. Please plant 🥬.")

    print("\n-------------------------------")
    for row in garden_layout:
        print(row)
    print("-------------------------------")


garden_game()