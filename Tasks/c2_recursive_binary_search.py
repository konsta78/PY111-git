from typing import Sequence, Optional
import random as r

arr_ = [r.randint(2, 7) for i in range(10)]
arr_.sort()

def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    return None

if __name__ == "__main__":
    print(arr_)
    print(binary_search(5, arr_))
