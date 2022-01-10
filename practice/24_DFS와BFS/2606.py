import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  x,y = map(int,sys.stdin.readline().split())
  graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

answer = []

visitied = [False]*(N+1)

def bfs(graph,start,visitied):
  queue = deque([start])
  visitied[start] = True

  while queue:
    v = queue.popleft()
    answer.append(v)
    graph[v].sort()
    for i in graph[v]:
      if visitied[i]==False:
        visitied[i] = True
        queue.append(i)


bfs(graph,1,visitied)
print(len(answer)-1)
