n = int(input())
sum = 0
product= 0

number = int(input())

if n > 10 and number not in [1,2]:
    print("WRONG INPUT AND INVALID CHOICE")

elif n > 10:
    print("WRONG INPUT")

elif number not in [1,2]:
    print("INVALID CHOICE")

elif number == 1:
    for num in range(1, n + 1, 1):
        sum = sum + num
    print("SUM:",sum)

elif number == 2:
    k = 1
    for i in range(1, n+1):
        k = k*i
    print(f"SUM:{sum(n)}")
    



elements = int(input())

List = input()

l = List.split()

list2 = []

for i in l:
    list2.append(int(i))
list2.sort()
print(l, list2[-1], list2[0])

