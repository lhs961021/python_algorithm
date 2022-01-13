import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
  A = sys.stdin.readline()

  if "push" in A:
    A,B = A.split()
    queue.append(B)
  elif "pop" in A:
    if len(queue)==0:
      print(-1)
    else:
      print(queue[0])
      queue.popleft()
  elif "size" in A:
    print(len(queue))
  elif "empty" in A:
    if len(queue)==0:
      print(1)
    else:
      print(0)
  elif "front" in A:
    if len(queue)==0:
      print(-1)
    else:
      print(queue[0])
  else:
    if len(queue)==0:
      print(-1)
    else:
      print(queue[len(queue)-1])