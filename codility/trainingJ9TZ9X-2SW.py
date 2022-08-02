# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    # write your code in Python 3.6
    m = len(A)
    if m==1:
        return A[0]

    m = Counter(A)
  
    for key, value in m.items():
      if value%2!=0:
        return key

