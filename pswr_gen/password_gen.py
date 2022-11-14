import random as ramd
from character_list import chars

def password_gen():
    print('Welcome to password generator!')
    pass_options = int(input('How many passwords do you want to be generated?: '))
    pass_length = int(input('What length do you want the passwords to have?: '))

    password_list = []

    for pwd in range(pass_options):
        password = ''
        for i in range(pass_length):
            if i == 0:
                while password.isalpha() is not True:
                    password = ramd.choice(chars)
            else:
                password += ramd.choice(chars)
        
        password_list.append(password)
    
    print(f'\nHere are your {pass_options} password options:')
    for i in range(len(password_list)):
        print(f'{i+1}. {password_list[i]}')


if __name__ == '__main__':
    password_gen()