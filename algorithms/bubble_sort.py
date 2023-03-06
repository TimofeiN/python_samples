"""
Modification of bubble sort for better time results.
"""
from random import randint
from timeit import timeit


def bubble_fst(lst):
    n = 1

    while n < len(lst):
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n = n + 1
    return f'{lst}'


def bubble_snd(lst):
    n = 1
    while n < len(lst):
        count = 0
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count = count + 1
        if count == 0:
            break
        else:
            n = n + 1
    return f'{lst}'


my_lst = [randint(-100, 100) for _ in range(30)]
print(my_lst)
print(bubble_fst(my_lst))

my_lst = [randint(-100, 100) for _ in range(50)]
print(my_lst)
print(bubble_snd(my_lst))

my_lst = [randint(-100, 100) for _ in range(50)]
print(timeit("bubble_fst(my_lst[:])", globals=globals(), number=1000))
print(timeit("bubble_snd(my_lst[:])", globals=globals(), number=1000))

"""
Array 500 elements
47.7715118000051
39.248042899998836

Array 100 elements
1.6239667999907397
1.475253500015242

Array 50 elements
0.4158721000130754
0.38909939999575727  
"""
