import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = {}

for _ in range(N):
  x,y = map(int,sys.stdin.readline().split())
  graph[x]=y

for _ in range(M):
  u,v = map(int,sys.stdin.readline().split())
  graph[u]=v

def bfs():
  queue = deque([1])
  visited = [0]*101
  
  while queue:
    node = queue.popleft()
    
    for i in range(1,7):
      if node+i<=100:
        if node+i not in graph:
          if visited[node+i]==0 or visited[node+i] > visited[node]+1:
            queue.append(node+i)
            visited[node+i]=visited[node]+1
        else:
          z = graph[node+i]
          if visited[z] == 0 or visited[z] > visited[node]+1:
            queue.append(z)
            visited[z] = visited[node]+1
            
  return visited[100]

print(bfs())
