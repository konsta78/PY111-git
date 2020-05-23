"""
My little Queue
"""
from typing import Any

queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global queue
    queue.append(elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global queue
    if queue:
        deq = queue[0]
        del(queue[0])
    else:
        deq = None
    return deq


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global queue
    if ind <= len(queue):
        peek_queue = queue[ind]
    else:
        peek_queue = None
    print(ind)
    return peek_queue


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global queue
    queue = []
    return None

if __name__ == "__main__":
    pass