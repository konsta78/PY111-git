"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global stack
    stack.insert(0, elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global stack
    if stack:
        pop_elem = stack[0]
        del(stack[0])
    else:
        pop_elem = None
    return pop_elem


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global stack
    if ind <= len(stack):
        peek = stack[ind]
    else:
        peek = None
    return peek


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global stack
    stack = []
    return None

if __name__ == "__main__":
    push(10)
    print(stack)
    push(7)
    print(stack)
    print(pop(), stack)
    print(peek(0), stack)
    print(clear(), stack)