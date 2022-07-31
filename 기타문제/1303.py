import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = []

for _ in range(M):
  graph.append(list(sys.stdin.readline().rstrip()))

def bfs(x,y,team,graph,visited):
  cnt = 0
  queue = deque()
  queue.append((x,y))
  
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  visited[x][y] = 1
  
  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx<0 or nx>=M or ny<0 or ny>=N:
        continue
      
      if visited[nx][ny]==0 and graph[nx][ny]==team:
        visited[nx][ny] = 1
        queue.append((nx,ny))
        cnt += 1

  return (cnt+1)**2

visited = [[0]*N for _ in range(M)]

W = 0
B = 0

for i in range(M):
  for j in range(N):
    if visited[i][j]==0:
      if graph[i][j]=="W":
        w = bfs(i,j,"W",graph,visited)
        W += w
      else:
        b = bfs(i,j,"B",graph,visited)
        B += b

print(W,B)