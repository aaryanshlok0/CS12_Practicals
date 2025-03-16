#program that prints no of seconds in a year
year = int(input("1. Common year:\n2. Leap year:\nEnter your choice: "))
if year == 1:
    print(f"Number of seconds in a year: {24 * 60 * 60 * 365}")
elif year == 2:
    print(f"Number of seconds in a leap year: {24 * 60 * 60 * 366}")
else:
    raise ValueError("Invalid input! Please try again.")
