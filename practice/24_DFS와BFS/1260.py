import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  x,y = map(int,sys.stdin.readline().split())
  graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

visitied = [False]*(N+1)

def dfs(graph,v,visitied):
  visitied[v] = True
  print(v,end=" ")
  graph[v].sort()
  for i in graph[v]:
    if visitied[i]==False:
      dfs(graph,i,visitied)

def bfs(graph,start,visitied):
  queue = deque([start])
  visitied[start] = True

  while queue:
    v = queue.popleft()
    print(v,end=" ")
    graph[v].sort()
    for i in graph[v]:
      if visitied[i]==False:
        visitied[i] = True
        queue.append(i)
      

dfs(graph,V,visitied)
print()
visitied = [False]*(N+1)
bfs(graph,V,visitied)

