list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("the element of list one is:",list1)
print("the element of the list two is:",list2)
s1 = 0
s2 = 0
if(len(list1)==len(list2)):
    print("list have same length")
else:
    print("list have different length")
for i in range(len(list1)):
    s1 = s1 + list1[i]
print("the sum of first list is",s1)
for i in range(len(list2)):
    s2 = s2 + list2[i]
print("the sum of list2 is",s2)
if(s1==s2):
    print("the sum of list have same")
else:
    print("sum of list is different")
print("the common element of the list is:")
for i in list1:
    for j in list2:
        if i == j:
          print(i)








