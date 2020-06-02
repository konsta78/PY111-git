def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise  ValueError("Error!")
    elif n < 2: return 1
    else:
        return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError("Error!")
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


if __name__ == "__main__":
    print(factorial_recursive(4))
    print(factorial_iterative(4))