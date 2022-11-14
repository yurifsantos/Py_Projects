import random as ramd

def guess_num_hum(x):
    min_num = 1
    max_num = x
    ramd_num = ramd.randint(min_num, max_num)
    guess_num = 0
    first_guess = True
    chances = 3
    while guess_num != ramd_num and chances > 0:
        print(f"You still have {chances} chances left!")
        if first_guess is True:
            guess_num = int(input(f'Please, guess a number between 1 and {max_num}: '))
            first_guess = False
        else:
            guess_num = int(input("Guess again: "))

        if guess_num < ramd_num:
            print(f'{guess_num} is lower than the picked number!')
            chances -= 1
        elif guess_num > ramd_num:
            print(f'{guess_num} is higher than the picked number!')
            chances -= 1

    if chances == 0:
        print(f"Sorry, your chances ran out! The correct number was {ramd_num}")
    else:
        print(f"You're right! The number picked was {ramd_num}")


def guess_num_machine():
    min_num = 1
    max_num = int(input("Please, input the maximum number the scrpit can guess: "))
    chances = 9
    reply = ''
    while reply != 'c' and chances > 0:
        print(f"The script has {chances} chances left")
        guess = ramd.randint(min_num, max_num)
        reply = input(f"The script guessed {guess}. Is the guess [L]ower, [H]igher or [C]orrect than the picked number?: ").lower()
        if reply == 'l':
            min_num = guess + 1
            chances -= 1
        elif reply == 'h':
            max_num = guess - 1
            chances -= 1

    if chances == 0:
        print("You won! The script couldn't guess your number!")
    else:
        print(f"The script guessed right! The number was {guess}!")

if __name__ == '__main__':
    
    mode = int(input("[1] is for you to guess and [2] the script will try to guess. Please choose the mode: "))
    if mode == 1:
        guess_num_hum(25)
    elif mode == 2:
        guess_num_machine()