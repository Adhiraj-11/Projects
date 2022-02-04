str1=input("enter string: ")
str2=''
a=input("encrypt the string?(yes/no): ")
if a=='yes':
    rot=int(input("enter rotation(0 for not defined): "))
    if rot==0:
        for i in str1:
            b=ord(i)
            str2+=chr(b+13)
    else:
        for i in str1:
            b=ord(i)
            str2+=chr(b+rot)
    print("encrypted string: ",str2)
    print("decrypted string: ",str1)
else:
    print("the string is: ",str1)