"""
My little Stack
"""
from typing import Any

stack = [1, 3, 5, 7]
#stack.remove()

def push(stack, elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    stack.append(elem)
    #print(elem)
    return stack


def pop(stack) -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    last_elem = stack[-1]
    stack.pop()
    return last_elem


def peek(stack, ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if ind <= len(stack):
        peek = stack[ind]
    else:
        peek = None
    return peek


def clear(stack) -> None:
    """
    Clear my stack

    :return: None
    """
    stack = []
    return stack

push(stack, 9)
print(stack)
last_elem = pop(stack)
print(stack, last_elem)
print(clear(stack))
print(peek(stack, 2))
print(peek(stack, 8))