str=input("enter registeration number:")
d=0
c=0
l = []
for i in str:
    if i.isdigit():
        l.append(int(i))
    else:
        l.append(i)
print(l)
length = len(str)
for i in range (0,length):
    if (i<=1 or i>=5):
        if (type(l[i] == int)):
            print("yes1")
        else:
            print("no")
    if (2<=i or i<=4):
        if (type(l[i] == str)):
            print("yes")
        else:
            print("no")