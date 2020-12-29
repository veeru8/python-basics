# python program for sum of a given number
n=int(input("enter the number:="))
sum=0
while n!=0:
    remainder=n%10
    sum=sum+remainder
    n=n//10
print(sum)
