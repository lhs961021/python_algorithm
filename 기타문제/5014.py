import sys
from collections import deque

F,S,G,U,D = map(int,sys.stdin.readline().split())

def bfs(start):
  graph = [0]*(F+1)
  q = deque([start])
  visited = [False]*(F+1)
  visited[start] = True
  d = [U,-D]

  while q:
    x = q.popleft()
    if x==G:
      return graph[G]
    for i in range(2):
      nx = x+d[i]
      if F>=nx>0 and not visited[nx]:
        visited[nx] = True
        graph[nx] = graph[x] + 1
        q.append(nx)
  
  if graph[G]==0:
    return "use the stairs"
    
print(bfs(S))