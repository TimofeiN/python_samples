"""
Recursion example.
Calculator works with user's numbers and finish work only when user enter "0".
"""


def calc(a, b, operation):
    a = int(a)
    b = int(b)
    if operation == '+':
        res = a + b
    elif operation == '-':
        res = a - b
    elif operation == '*':
        res = a * b
    else:
        res = a / b
    return res


def timeless_calc():
    action = input('Enter operation (+, -, *, / or 0 to exit): ')
    if action == '0':
        print('end')
    elif action in ['+', '-', '*', '/']:
        fst_num = input('Enter first number: ')
        if not fst_num.isdigit():
            print(f'"{fst_num}" is not a number')
            timeless_calc()
        else:
            pass
        snd_num = input('Enter second number: ')
        if not snd_num.isdigit():
            print(f'"{snd_num}" is not a number')
            timeless_calc()
        elif snd_num == '0' and action == '/':
            print('zero division')
            timeless_calc()
        else:
            print(f'Result = {calc(fst_num, snd_num, action)}')
            timeless_calc()
    else:
        timeless_calc()


timeless_calc()
