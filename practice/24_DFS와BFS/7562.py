import sys
from collections import deque

N = int(sys.stdin.readline())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]


def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny<0 or nx>m-1 or ny>m-1:
        continue

      if nx==a and ny==b:
        print(graph[x][y]+1)
        return  
      
      if graph[nx][ny]==0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
        

for _ in range (N):
  m = int(sys.stdin.readline())
  graph = [[0]*m for _ in range(m)]
  
  x,y = map(int,sys.stdin.readline().split())

  a,b = map(int,sys.stdin.readline().split())

  if x==a and x==b:
    print(0)
  else:
    bfs(x,y)

  






