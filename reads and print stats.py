#ascii range of digits 48-57
#ascii range of uppercase 65-90
#ascii range of lowercase 97-122
#ord is ordinal numebr and returns ascii value of a character 

line=input("Enter a line: ")
upper=lower=digit=alphabets=0
for ch in line:
    if ord(ch) in range(48,58):
        digit+=1
    elif ord(ch) in range(65,91):
        upper+=1
        alphabets+=1
    elif ord(ch) in range(97,123):
        lower+=1
        alphabets+=1
print(f"No of lowercase characters  are {lower}")
print(f"No of uppercase characters are {upper}")
print(f"No of alphabets are {alphabets}")
print(f"No of digits in are {digit}")

