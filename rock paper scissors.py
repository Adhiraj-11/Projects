import random

player_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_choice = input('Type rock/paper/scissors or Q to quit: ').lower()

    if user_choice == "q":
        break

    if user_choice not in options:
        print('Enter a valid option: ')
        continue

    random_number = random.randint(0, 2)
 
    computer_pick = options[random_number]

    print("Computer picked", computer_pick)

    if user_choice == 'rock' and computer_pick == 'scissors':
        print('You Won')
        player_wins += 1
    elif user_choice == 'paper' and computer_pick == 'rock':
        print('You Won')
        player_wins += 1
    elif user_choice == 'scissors' and computer_pick == 'paper':
        print('You Won')
        player_wins += 1

    elif user_choice == computer_pick:
        print("Its a draw! ")
        
    else:
        print("You lost, Computer wins! ")
        computer_wins += 1

print('You won', player_wins , "times!")
print("computer won", computer_wins, "times!")
print("Goodbye!")

input()
