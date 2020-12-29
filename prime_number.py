# python program for prime number
n=int(input("Enter the number:="))
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
        break
if(count==0&n!=1):
    print("%d is a prime number"%n)
else:
    print("%d is not a prime number"%n)
