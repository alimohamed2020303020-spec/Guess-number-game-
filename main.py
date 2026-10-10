import random

def get_number(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('Enter a number only')
            continue
        if 1 <= n <= 100:
            return n
        print('invalid number (should be between 1 and 100)')

BIG = ('big', 'bigger', 'greater', 'great')
SMALL = ('small', 'smaller', 'less')

title = ' Guess number game '
x = title.center(60, '=')
print(x.title())

while True:
    c_num = random.randint(1, 100)
    p_num = get_number('Choose your secret number : ')
    low, high = 1, 100  

    while True:
        p_guess = get_number('Enter your guess : ')
        if p_guess == c_num:
            print('You win!')
            break
        elif p_guess > c_num:
            print('computer : bigger')
        else:
            print('computer : smaller')

        c_guess = random.randint(low, high)
        print(f'The computer chose {c_guess}')
        if c_guess == p_num:
            print('The computer wins!')
            break

        if c_guess > p_num:
            right = BIG
        else:
            right = SMALL

        confirm = input('player : ').lower()
        while confirm not in right:
            print('Play fair and honest')
            confirm = input('player : ').lower()

        if c_guess > p_num:
            high = c_guess - 1
        else:
            low = c_guess + 1

    again = input('Do you want to play again : ')
    if again.lower() not in ('y', 'yes', 'ye', 'yeah', 'yea'):
        print('Good bye!')
        break
