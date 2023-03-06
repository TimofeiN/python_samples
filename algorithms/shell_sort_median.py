"""
Function finds a median of array with a shell sort.
Time results for arrays lengths 10, 100, 1000.
"""
from random import randint
from timeit import timeit


def med_shell_sort(m):
    lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    d = round(len(lst) // 2)

    while d > 0:
        j = 0
        while j < d:

            for i in range(j, (len(lst) - d), d):
                if lst[i] > lst[i + d]:
                    lst[i], lst[i + d] = lst[i + d], lst[i]
                    n = i
                    while n >= d and lst[n] < lst[n - d]:
                        lst[n], lst[n - d] = lst[n - d], lst[n]
                        n = n - d
            j = j + 1

        d = d // 2
    return f'Median = {lst[m]}'


print(timeit("med_shell_sort(5)", globals=globals(), number=1000))
print(timeit("med_shell_sort(50)", globals=globals(), number=1000))
print(timeit("med_shell_sort(500)", globals=globals(), number=1000))

"""
Time results:
0.026310100016416982
0.33227079999051057
4.856045599997742
"""
