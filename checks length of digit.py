#checks length of digits betwenn 0-999

num=int(input("Enter a number between 0-999: "))
if num>=0 and num<10:
    print(f"{num} is a single digit number")
elif num>=10 and num<100:
    print(f"{num} is a double digit number")
elif num>=100 and num<1000:
    print(f"{num} is a three digit number")
else:
    raise ValueError("The number entered is out of range!")