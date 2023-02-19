a=input("enter the first number:")
b=input("enter the second number:")
c=input("enter the last number:")
if(a > b and a > c):
    print(" largest number is:",a)
elif(b > a and b > c):
    print("largest number is:",b)
else:
    print("largest number is:",c)