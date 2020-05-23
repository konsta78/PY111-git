"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any
import random as r

queue = [[] for i in range(11)] # priorities are form 0 to 5

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global queue
    queue[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global queue
    for i in range(len(queue)):
        if queue[i]:
            deq = queue[i][0]
            del(queue[i][0])
            return deq
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global queue
    if queue[priority]:
        peek_que = queue[priority][ind]
    else:
        peek_que = None
    return peek_que


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global queue
    queue = [[] for i in range(11)]
    return queue

if __name__ == "__main__":
    for i in range(10):
        enqueue(i, r.randint(0,10))

    print(queue)
    print(dequeue())
    print(queue)
    print(peek(0, 4))
    print(peek(0, 3))
    print(peek(0, 2))