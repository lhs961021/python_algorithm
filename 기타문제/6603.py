import sys
from collections import deque
import itertools


z = 0

while z==0:
  a = deque(map(int,sys.stdin.readline().split()))
  k = a[0]
  if k == 0:
    break
  else:
    a.popleft()
    m = list(itertools.combinations(a,6))
    for i in m:
      print(*i)
    print()