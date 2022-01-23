import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

q = deque([i for i in range(1,N+1)])

print("<",end="")

for i in range(N):
  q.rotate(-(K-1))
  print(q.popleft(),end="")
  if i==N-1:
    print(">")
  else:
    print(", ",end="")
    
