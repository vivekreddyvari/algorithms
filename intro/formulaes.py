from dataclasses import dataclass
from time_wrapper import timer


@dataclass
class Formulae:
    """ This class supplies best performing mathematical formulaes"""

    @timer
    def sum_of_x_numbers(self, x: int):
        """ returns sum of x numbers"""
        return (x * (x + 1)) / 2


if __name__ == "__main__":
    F = Formulae()
    print(F.sum_of_x_numbers(30))



@dataclass
class BigONotation:
    """
    f(n)    Name
    1       Constant
    log n   Logarithmic
    n       Linear
    n log n Log linear
    n**2    Quadratic
    n**3    Cubic
    2ˆn     Exponential
    """