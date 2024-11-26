from datetime import datetime

# age = int(input("Enter your age in years: "))
# months = age * 12
# print("Total months " + str(months))
# days = int(age * 365.25)
# print("Total days".format (days))
# hours = int(days * 24)
# print(f"Total seconds {hours} hours")
# seconds = int(hours * 3600)
# print("Total seconds: ", seconds," seconds")
leaf = "\U0001F331"
flower = "\U0001F337"
corn = "\U0001F33D"
watermelon = "\U0001F349"
orange = "\U0001F34A"
grape = "\U0001F347"

print(leaf, flower, corn, watermelon, orange, grape)

VALID_PLANTS = {
    '🌱': "\U0001F331",
    '🌷': "\U0001F337",
    '🌽': "\U0001F33D",
    '🍉': "\U0001F349",
    '🍊': "\U0001F34A",
    '🍇': "\U0001F347"
}

def is_valid_plant(plant):
    return plant in VALID_PLANTS

def is_valid_number(num):
    return num.isdigit()

def get_max_width(plants, numbers):
    try:
        return max(int(num) for plant, num in zip(plants, numbers) if is_valid_plant(plant) and is_valid_number(num))
    except ValueError:
        return 0

def generate_garden(plants, numbers):
    max_width = get_max_width(plants, numbers)
    if max_width == 0:
        return "/\\\n\\/\n"

    garden = [f"/{'-' * (max_width * 2)}\\"]
    for plant, num in zip(plants, numbers):
        if is_valid_plant(plant) and is_valid_number(num):
            row = VALID_PLANTS[plant] * int(num)
            garden.append(f"|{row.ljust(max_width * 2)}|")
    garden.append(f"\\{'-' * (max_width * 2)}/")
    return "\n".join(garden)

def garden_orders():
    order_number = 1
    while True:
        print(f"ORDER {order_number}")
        plants = input("What plants would you like in your garden (type 'exit' to quit)?\n")
        if plants.lower() == "exit":
            print("Bye, hope to see you soon :)")
            break
        numbers = input("How many of each plant do you want to plant (type 'exit' to quit)?\n")
        if numbers.lower() == "exit":
            print("Bye, hope to see you soon :)")
            break
        if len(plants) != len(numbers):
            print("Error: The number of plants must match the number of quantities entered.")
            continue
        if all(is_valid_plant(plant) and is_valid_number(num) for plant, num in zip(plants, numbers)):
            print(generate_garden(plants, numbers))
            order_number += 1
        else:
            print("Please enter valid plants and numbers.")

garden_orders()