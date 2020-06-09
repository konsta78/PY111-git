import numpy as np

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    a = np.zeros((shape[0], shape[1]))
    a[a.shape[0]-1, 0] = 1
    for i in range(shape[0] - 1, 0, -1): # строки
        for j in range(shape[0] - 1): # столбцы
            if a[i, j] != 0 and a[i, j] !=1:
                if i > 1:
                    a[i - 2, j + 1] += 2 + a[i, j]
                if j < shape[1] - 2:
                    a[i - 1, j + 2] += 2 + a[i, j]
            elif a[i, j] == 1:
                a[i - 2, j + 1] = 2
                a[i - 1, j + 2] = 2
    print(a)
    return int(a[point[0], point[1]])


if __name__ == "__main__":
    # m = n = 3
    # a = np.zeros((m, n))
    # print(a)
    #calculate_paths((8, 8), (0, 7))
    print(calculate_paths((6, 6), (0, 0)))