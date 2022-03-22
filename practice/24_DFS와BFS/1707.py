import sys
from collections import deque

K = int(sys.stdin.readline())

red = 2
blue = 3

def bfs(x,V):
  queue = deque([x])
  if visited[x]==0:
    visited[x] = blue
    
  while queue:
    x = queue.popleft()
    color = visited[x]
    
    for i in graph[x]:
      if visited[i]==False:
        if color==red:
          visited[i] = blue
        else:
          visited[i] = red  
        queue.append(i)
      elif visited[i]==red:
        if color==red:
          print("NO")
          return False
      elif visited[i]==blue:
        if color==blue:
          print("NO")
          return False
  return True

for _ in range(K):
  flag = 0
  V,E = map(int,sys.stdin.readline().split())

  graph = [[] for _ in range(V+1)]
  visited = [False]*(V+1)

  for _ in range(E):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

  for k in range(1,V+1):
    if not bfs(k,V):
      flag = 1
      break
  if flag==0:
    print("YES")
    
  

  
