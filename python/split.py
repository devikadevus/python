s=str(input("enter line of text:"))
count=dict()
word=s.split()
for x in word:
    if x in count:
        count[x] += 1
    else:
        count[x]=1
print(count)
