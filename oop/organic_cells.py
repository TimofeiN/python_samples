"""
Class works with organic cells, consisting of cells.
The class have methods for overloading arithmetic operators:
- Addition. Union of two cells. In this case, the number of cells of the common cell is equal to the sum of the cells of
the original two cells.
- Subtraction. Two cells are involved. Works only if the difference in the number of cells of two cells is greater
zero, otherwise display the appropriate message.
- Multiplication. A common cell is created from two. The number of cells in a common cell is the product of the number
of cells in these two cells.
- Division. A common cell is created from two. The number of cells in a common cell is defined as an integer division
of the number cells of these two cells.

The make_order() method, which takes an instance of the class and the number of cells in the row. This method allows you
to organize cells in rows.
Returns a string like *****\n*****\n*****..., where the number of cells between \n is equal to the given argument.
If there are not enough cells to form a row, then all the remaining ones are recorded in the last row.
For example, the number of cells in a cell is 12, and the number of cells in a row is 5. In this case, the make_order()
method will return:
string:
    *****
    *****
    **
"""

from abc import abstractmethod


class Cell:
    def __init__(self, cells, line=0):
        self.cells = cells
        self.line = line

    def __str__(self):
        return f'cell with {self.cells} units'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print(f'Unpossible to subtract difference less than 0')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        return Cell(self.cells / other.cells)

    @abstractmethod
    def make_order(self, cells, line):
        x = cells // line
        y = cells % line
        output = (f'*' * line + f"\n") * x + f'*' * y
        return output


first_cell = Cell(40)
second_cell = Cell(30)

res = first_cell + second_cell
print(res)
print(first_cell.make_order(12, 5))
