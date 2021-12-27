import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <0:
        print("Please pick a positive number next time ")
        quit()
else:
    print("Please type a valid input ")
    quit()

r = random.randint(0, top_of_range)

guesses = 0  

while True:
    guesses += 1
    user_guess = input("Guess a number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time ")
        continue

    if user_guess == r:
        print ("You got it correct! ")
        break
    else:
        if user_guess > r:
            print("Your guess is above the required number! ")
        else:
            print("Yor guess is below the required number ")

print('You got it in' ,  guesses,  'guesses! ')      

input()



