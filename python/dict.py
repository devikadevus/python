dic={'anu':5,'reva':4,'maya':10,'vinay':11}
l=list(dic.items())
l.sort()
d=dict(l)
print("assending order is:", d)
l=list(dic.items())
l.sort(reverse= True)
d=dict(l)
print("decending orde is:",d)

