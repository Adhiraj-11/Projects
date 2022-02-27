#Q2
# 5**9 = 1953125
# 3//2 = 1
# 7//3 = 2
# 7/3 = 2.3333333333333335
# 6 == 6 = True
# a = 20; a+= 30; a%=3; print(a) = 2
# True * False = 0
# True & False = False
# True and False = False
# ((6>3) and (7<4) or (18==3)) and (9>3) = False
# True is False = False
# False in ‘False’ = error
# ((True == False) or (False > True)) and (False <= True) = False

#Q3
s1 = "Nice to have it"
s2 = "here"

add = s1 + " " + s2
print(add)

#Q4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
index1 = a[3]
index2 = index1[1]
index3 = index2[2]
final_index = index3[0]
print(final_index)

#Q5
a.append(s1)
a.append(s2)
a.insert(0,s2)
a.insert(0,s1)
print(a)

#Q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
    if i % 2 == 0:
        print(i)
    if i == 237:
        break
    
#Q7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#Q8
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
string = str(input())
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

#Q9
n = input()
print (int(n) + int(n*2) + int(n*3))

#Q11
words = input()
words_list = words.split(",")
words_list.sort()
listToStr = ','.join(words_list)
print(listToStr)

#Q13
str_num = input()
Letters = 0
digits = 0
for i in str_num:
    if i.isalpha() == True:
        Letters += 1
    if i.isdigit() == True:
        digits += 1
print(Letters)
print(digits)


