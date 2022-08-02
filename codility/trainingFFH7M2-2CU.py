# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

def solution(A, K):
    # write your code in Python 3.6

    m = len(A)

    if m==0:
        return A

    A = deque(A)

    z = K%m

    A.rotate(z)

    return list(A)
