n=int(input("enter the limit:"))
li=[]
s=(0)
for i in range(n):
    x = str(input("enter a names :"))
    li.append(x)
for i in li:
    r=i.count('a')
    s=s+r
print(s)

