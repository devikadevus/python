str=input("enter a sring:")
for i in  str:
    char=str[0]
    str=str.replace(char,'$')
    str=char + str[1:]
print(str)