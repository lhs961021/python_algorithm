import sys
from collections import deque

n = int(sys.stdin.readline())
x,y = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(x,y):
  
  queue = deque()
  queue.append((x,0))

  while queue:
    idx,cost = queue.pop()
    
    visited[idx]=True
    for i in graph[idx]:
      if visited[i]==False:
        if i==y:
          return cost+1
        queue.append((i,cost+1))
  
  return -1
  
print(bfs(x,y))
