"""
Realisation of matrix class.
It's possible to addict matrices,
to show matrix in usual form.
"""


class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        output = ''
        for el in self.numbers:
            el = [str(num) for num in el]
            output += f'|{" ".join(el)}|\n'
        return output

    def __add__(self, other):
        result = []
        for idx in range(len(self.numbers)):
            line = []
            for i in range(len(self.numbers[idx])):
                num = self.numbers[idx][i] + other.numbers[idx][i]
                line.append(num)
            result.append(line)
        return Matrix(result)


first_matrix = Matrix([[31, 22, 1], [37, 43, 1], [51, 86, 1]])
second_matrix = Matrix([[3, 2, 1], [3, 4, 1], [5, 8, 1]])
new_m = first_matrix + second_matrix
print(first_matrix)
print(second_matrix)
print(new_m)
