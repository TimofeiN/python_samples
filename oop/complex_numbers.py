"""
A program to add and multiply two hexadecimal numbers.
Each number is represented as an array, whose elements are the digits of a number.
For example user print: A2 & C4F.
Summ =  [‘C’, ‘F’, ‘1’],
Multiply = [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict

fst = list(input('Input first number: '))
snd = list(input('Input second number: '))

# Solution 1 - collections module:
numbers_d = defaultdict(list)
numbers_d['fst'] = fst
numbers_d['snd'] = snd
f_num = int((''.join(numbers_d['fst'])), 16)
s_num = int((''.join(numbers_d['snd'])), 16)

print(f'Summ of numbers: {list(hex(f_num + s_num).upper())[2:]}')
print(f'Multiplication of numbers: {list(hex(f_num * s_num).upper())[2:]}\n')


# Solution 2 - OOP:
class Number:
    def __init__(self, num_lst):
        self.num_16 = int(''.join(num_lst), 16)

    def __add__(self, other):
        res = self.num_16 + other.num_16
        return hex(res).upper()[2:]

    def __mul__(self, other):
        res = self.num_16 * other.num_16
        return hex(res).upper()[2:]


f_num = Number(fst)
s_num = Number(snd)

print(f'Summ of numbers: {f_num + s_num}')
print(f'Multiplication of numbers: {f_num * s_num}')
