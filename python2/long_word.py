n=int(input("enter the number of word:"))
list=[]
for i in  range(n):
    x=input("enter the word:")
    list.append(x)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i) > max):
        max=len(i)
        temp=i
print("the longest word of length is:",temp,"and its length is:",max)
