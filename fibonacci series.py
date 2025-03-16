#this program prints the first n numbers of fibonacci series
#using for loop

a,b=0,1
n=int(input("Enter the no of terms you want fibonacci for: "))
fibonacci=(a,)
if n<=0:
    raise ValueError("Please input a number greater than zero.")
elif n>0:
    for i in range(1,n+1):
        fibonacci+=(b,)
        a,b=b,a+b
print(fibonacci)



#using while loop
a,b=0,1
fibonacci=(a,)
n=int(input("Enter no of terms you want for fibonacci series: ")) 
count= n-2 #n-2 as we have already defined 2 terms in the beginning
if n<=0:
    raise ValueError("Invalid input")
elif n>0:
    while count>=0:
        fibonacci+=(b,)
        a,b=b,a+b
        count-=1
    print(fibonacci)

#using binets formula:
