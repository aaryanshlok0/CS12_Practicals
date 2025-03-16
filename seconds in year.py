#program that prints no of seconds in a year
year=int(input("1. Common year\n2. Leap year: "))
if year==1:
    print(f"No of seconds in a year is {24*60*60*365}")
elif year==2:
    print(f"No of seconds in a leap year is {24*60*60*366}")
else:
    raise ValueError("Inavlid input!Please try again")
