import pygame 

print('Welcome to a trivia quiz')

player = input("Enter your name: ")
"name: "

game_running = True

while game_running: 
    x = input("type Y to continue\ntype N to quit ")
    if x in (["yes", "y"]):
        print("OKAY! Let's play!")
        break
    elif x in (["no", "n"]):
        game_running = False
    else:
        print("Enter a valid input")
        continue

    score = 0

print("1)How many alphabets are there in English? " )
answer = input("a)23\nb)24\nc)25\nd)26 " )

if answer in (["d", "D"]):
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("2) What is 5 + 5?")
answer = input("a)9\nb)10\nc)11\nd)12 " )

if answer in (["b", "B"]):
    print("correct!")
    score += 1
else:
    print("Incorrect!")


print("3)which is the largest number?")
answer = input("a)500\nb)200\nc)400\nd)100 " )

if answer in (["a", "A"]):
    print("correct!")
    score += 1
else:
    print("Incorrect!")


print("4)Identify the odd one out. ")
answer = input("a)Dog\nb)Cat\nc)Pencil\nd)Cow ")

if answer in (["c", "C"]):
    print("correct!")
    score += 1
else:
    print("Incorrect!")


print("5)How many Vowels are there in English alphabets? " )
answer = input("a)5\nb)4\nc)6\nd)7 ")

if answer in (["a", "A"]):
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print(" congratulations " + player + " You got " + str(score) + " questions correct! ")

input()
