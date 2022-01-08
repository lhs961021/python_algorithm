import sys
from collections import deque

N = int(input())

stk = deque()

for _ in range(N):
  A = sys.stdin.readline()

  if "push_front" in A:
    A, B= A.split()
    stk.appendleft(B)
  elif "push_back" in A:
    A, B= A.split()
    stk.append(B)
  elif "pop_front" in A:
    if len(stk)==0:
      print(-1)
    else:
      a = stk[0]
      stk.popleft()
      print(a)
  elif "pop_back" in A:
    if len(stk)==0:
      print(-1)
    else:
      b = stk[len(stk)-1]
      stk.pop()
      print(b)
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
  else:
    if len(stk)==0:
      print(-1)
    else:
      print(stk[0])
  
    
