class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length * self.breadth)
    def perimeter(self):
        return(2 *(self.length + self.breadth))
l1=int(input("enter the length1:"))
b1=int(input("enter the breadth1:"))
r1=Rectangle(l1,b1)
print("area of rectangle1:",r1.area())
print("perimeter of rectangle 1:",r1.perimeter())
l2=int(input("enter the length2:"))
b2=int(input("enter the breadth2:"))
r2=Rectangle(l2,b2)
print("area of rectangle 2:",r2.area())
print("perimeter of rectangle 2:",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1 > a2:
    print("area of the rectangle 1 is heigh")
elif a1 == a2:
    print("area are equal")
else:
    print("area of the rectangle 2 is heigh")





