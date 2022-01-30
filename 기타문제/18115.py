import sys
from collections import deque

N = int(sys.stdin.readline())

graph = deque([i for i in range(1,N+1)])

s = deque([]*N)

answer = list(map(int,sys.stdin.readline().split()))

for i in range(len(answer)-1,-1,-1):
  a = graph.popleft()
  if answer[i]==1:
    s.appendleft(a)
  elif answer[i]==2:
      s.insert(1,a)
  elif answer[i]==3:
    s.append(a)

print(*s)