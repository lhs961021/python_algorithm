import sys
from collections import deque

N = list(sys.stdin.readline().rstrip())

M = deque(N)
answer = deque()

Z = int(sys.stdin.readline())



for _ in range(Z):
  A = sys.stdin.readline().rstrip()
  if A=='L':
    if len(M)!=0:
      answer.appendleft(M.pop())
  elif A=='D':
    if len(answer)!=0:
      M.append(answer.popleft())
  elif A=='B':
    if len(M)!=0:
      M.pop()
  else:
    A,B = A.split()
    M.append(B)


print("".join(M)+"".join(answer))  
  