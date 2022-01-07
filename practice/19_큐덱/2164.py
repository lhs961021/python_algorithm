import sys
from collections import deque


N = int(sys.stdin.readline())

data = deque(i for i in range (1,N+1))

while len(data)!=1:
  data.popleft()
  data.rotate(-1)

print(*data)
