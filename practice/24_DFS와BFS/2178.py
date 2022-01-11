import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = []


for _ in range (N):
  graph.append(list(map(int, input())))

def bfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y
      if nx<0 or ny<0 or ny>N-1 or nx>M-1:
        continue
      if graph[ny][nx]==0:
        continue
      if graph[ny][nx]==1:
        graph[ny][nx] = graph[y][x] + 1
        queue.append((nx,ny))
  return graph[N-1][M-1]
      
print(bfs(0,0))


