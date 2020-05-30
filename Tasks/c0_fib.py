def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    a = 0
    b = 1
    sum = a + b # 2
    for i in range(1, n+1):
        a = b
        b = sum
        sum = a + b
        print(a, b, sum)
    return sum


if __name__ == "__main__":
    fib_iterative(8)