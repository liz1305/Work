from datetime import datetime

age = int(input("Enter your age in years: "))
months = age * 12
print("Total months " + str(months))
days = int(age * 365.25)
print(f"Total days {days} days")
hours = int(days * 24)
print(f"Total seconds {hours} hours")
seconds = int(hours * 3600)
print("Total seconds: ", seconds," seconds")

