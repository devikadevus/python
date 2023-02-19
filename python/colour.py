n=int(input("enter the number of colour:"))
list=[]
for i in range(n):
    a=input("enter the colour name:")
    list.append(a)
print(list)
print("enter first colour is:",list[0])
print("enter the last colour is:",list[-1])