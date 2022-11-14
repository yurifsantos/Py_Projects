import random as ramd
import re
import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def is_wins(user, cpu):
    if (user == 'r' and cpu == 's') or (user == 'p' and cpu == 'r') or (user == 's' and cpu == 'p'):
        return True
    return False


def jokenpo():
    options = ['r', 'p', 's']
    user_score = 0
    cpu_score = 0
    try_again = 'y'
    while try_again == 'y':
        clear_screen()
        user_choice = ''
        while not re.match("[rps]", user_choice):
            print("Choose your weapon!")
            user_choice = input("[R]ock | [P]aper | [S]cissor: ").lower()
        
        print(f"Your choice was: {user_choice}")

        cpu_choice = ramd.choice(options)
        print(f"Your opponent chose {cpu_choice}")

        if user_choice == cpu_choice: print("It's a tie!")
        else: 
            score = is_wins(user_choice, cpu_choice)
            if score is True:
                user_score += 1
                print(f"You won! The score is {user_score} x {cpu_score}")
            else:
                cpu_score += 1
                print(f"I won! The score is {user_score} x {cpu_score}")

        print("Wanna try again? [y] to continue, or any other input to exit.")
        try_again = input().lower()
         

if __name__ == '__main__':
    jokenpo()