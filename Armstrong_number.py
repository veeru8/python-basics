#python program for to find whether it is a Armstrong number or not
#sum cubes equal to the given nuber
n=int(input("enter the number:"))
Number=n
Armstrong=0
while(n!=0):
    remainder=n%10
    Armstrong=Armstrong+(remainder*remainder*remainder)
    n=n//10
if(Armstrong==Number):
    print("ArmStrong number")
else:
    print("Not a AramStrong number")

