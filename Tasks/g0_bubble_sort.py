from typing import List
import random as r


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for j in range(len(container) - 1):
        for i in range(len(container) - 1 - j):
            if container[i] > container[i+1]:
                container[i], container[i+1] = container[i+1], container[i]

    return container


def test():
    l1 = [x for x in range(0, 10)]
    r.shuffle(l1)
    print(l1)
    for j in range(len(l1) - 1):
        for i in range(len(l1) - 1 - j):
            if l1[i] > l1[i+1]:
                l1[i], l1[i+1] = l1[i+1], l1[i]

    print((l1))

if __name__ == '__main__':
    test()