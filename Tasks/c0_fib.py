def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError("Error!")
    elif n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    fib1 = 0
    fib2 = 1
    fib = fib2 + fib1
    if n < 0:
        raise  ValueError("Error!")
    for i in range(2, n + 1):
        fib = fib2 + fib1
        fib1 = fib2
        fib2 = fib
    return fib


if __name__ == "__main__":
    print(fib_iterative(8))
    print(fib_recursive(8))