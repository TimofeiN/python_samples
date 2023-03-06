"""
Fabric consumption calculation:
V = size (for coat)
H = height (for suit)
To determine the fabric consumption for each type of clothing, use the following formulas:
for coats (V / 6.5 + 0.5),
for a suit (2*H + 0.3).
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def textile_calc(self):
        pass


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def textile_calc(self):
        textile = (2 * self.param) + 0.3
        return textile


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def textile_calc(self):
        textile = (self.param / 6.5) + 0.5
        return textile


suit = Suit(180)
print(suit.textile_calc)
coat = Coat(66)
print(coat.textile_calc)
