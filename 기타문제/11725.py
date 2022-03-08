import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [[] for _ in range(N+1)]

for _ in range(N-1):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque([1])

while queue:
  a = queue.popleft()
  visited[a] = True

  for i in graph[a]:
    if visited[i]==False:
      answer[i]=a
      queue.append(i)

for i in range(2,N+1):
  print(answer[i])

