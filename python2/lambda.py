a=int(input("enter the side of square:"))
s_area=lambda a:a*a
print("are of square is:",s_area(a))
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
r_area = lambda l,b:l * b
print("are of rectangle is:", r_area(l,b))
h=int(input("enter the base of triangle:"))
b=int(input("enter the height of triangle:"))
t_area = lambda b,h:5 * b * h
print("are of triangle is:", t_area(b,h))
