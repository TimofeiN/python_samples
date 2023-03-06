"""
Function counts a unique substrings in string.
Works with hash and set.

Example:
рара - 6 unique substrings

рар
ра
ар
ара
р
а
"""
import hashlib


def sub_str_searcher(my_str):
    sub_str_set = set()
    for i in range(len(my_str)):
        if i == 0:
            str_slice = my_str[i+1:-1]
        else:
            str_slice = my_str[(i+1):]
        sub_str = my_str[i]
        sub_str_set.add(hashlib.md5(sub_str.encode()).hexdigest())
        for n in range(len(str_slice)):
            sub_str += str_slice[n]
            sub_str_set.add(hashlib.md5(sub_str.encode()).hexdigest())
    return f'{len(sub_str_set)}'


test_str = 'papa'
print(sub_str_searcher(test_str))
