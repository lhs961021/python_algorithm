import sys
from collections import deque

N = int(input())

stk = deque()

for _ in range(N):
  A = sys.stdin.readline()

  if "push" in A:
    A, B= A.split()
    stk.append(B)
  elif "size" in A:
      print(len(stk))
  elif "empty" in A:
    if len(stk)==0:
      print(1)
    else:
      print(0)
  elif "back" in A:
    if len(stk)==0:
      print(-1)
    else:
      print(stk[len(stk)-1])
  elif "front" in A:
    if len(stk)==0:
      print(-1)
    else:
      print(stk[0])
  else:
    if len(stk)==0:
      print(-1)
    else:
      m = stk.popleft()
      print(m)
