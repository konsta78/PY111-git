from typing import Sequence, Optional
import random

arr_ = [random.randint(-10, 10) for _ in range(20)]

def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    arr.sort()
    l = 0
    r = len(arr)

    while r - l > 1:
        m = (l + r) // 2
        if elem > arr[m]:
            l = m
        else:
            r = m

    if elem == arr[l]:
        return l
    elif elem == arr[r]:
        return r
    else:
        return None


if __name__ == "__main__":
    a = binary_search(1, arr_)
    print(arr_)
    print(1, a)
