#program reads an integer N from keyboard computers and displays sum from N TO (2*N) if N is nonnegative
#if N is -ve then,it's the sum of numbers from 2*N to N including starting and ending points

num=int(input("Enter an integer: "))
sum=0
if num >=0:
    for a in range(num,num*2+1):
        sum+=a
elif num<0:
    for a in range(2*num,num+1):
        sum+=a
print(f"Sum of numbers is {sum}")    