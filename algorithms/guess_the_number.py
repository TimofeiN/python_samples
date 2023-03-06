"""
A simple game.
User need to guess the number between 1 and 100 in 10 turns.

Wrote with recursion.
"""


def guess_the_num(num=0, n=1):
    if n == 1:
        import random
        num = random.randint(1, 100)
        print('You need to guess the number in ten turns')
    u_num = int(input('Enter number: '))
    if n > 9:
        print(f'You loose,  = {num}')
        return
    elif u_num < num:
        print('Your number is less than expected')
        n = n + 1
        guess_the_num(num, n)
    elif u_num > num:
        print('Your number is greater than expected')
        n = n + 1
        guess_the_num(num, n)
    elif u_num == num:
        print(f'You win! (Turns {n})')
        return


guess_the_num()
