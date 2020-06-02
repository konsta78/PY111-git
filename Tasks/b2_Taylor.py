"""
Taylor series
"""
from typing import Union
from Tasks.c1_fact import factorial_iterative


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e_x = 1
    for i in range(1, 10):
        e_x += x**i / factorial_iterative(i)
    return e_x


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_x = x
    for n in range(1, 10):
        sin_x += (-1)**n * x**(2*n+1)/factorial_iterative(2*n+1)
    return sin_x

if __name__ == "__main__":
    print(ex(3))
    print(sinx(90))