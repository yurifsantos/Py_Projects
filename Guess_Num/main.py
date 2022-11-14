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
            guess_num = int(input("Next try: "))

        if guess_num < ramd_num:
            print(f'{guess_num} is lower than the picked number. Guess again!')
            chances -= 1
        elif guess_num > ramd_num:
            print(f'{guess_num} is higher than the picked number. Guess again!')
            chances -= 1

    if chances == 0:
        print(f"Sorry, your chances ran out! The correct number was {ramd_num}")
    else:
    print(f"You're right! The number picked was {ramd_num}")



if __name__ == '__main__':
    guess_num_hum(10)