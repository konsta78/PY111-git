"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

arr_ = []

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    index = 0
    min_elem = arr[index]
    for i in range(len(arr)):
        if arr[i] < min_elem:
            min_elem = arr[i]
            index = i
    return index


if __name__ == "__main__":
    min_search(arr_)