#python program for to find whether it is a pallindrome or not
n=int(input("enter the number:"))
reverse=0
original=n

while(n!=0):
    remainder=n%10
    reverse=(reverse*10)+remainder
    n=n//10
if(reverse==original):
    print("pallindrome")
else:
    print("not a pallindrome")
    
