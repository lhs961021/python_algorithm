import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for _ in range(N):
  graph.append(list(map(int,input())))

def bfs(x,y,crash,visitied):
  queue = deque()
  queue.append((x,y,crash))
  visited[x][y][crash] = 1

  while queue:
    x,y,crash = queue.popleft()

    if x==N-1 and y==M-1:
      return visited[x][y][crash]

    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y

      if nx<0 or ny<0 or nx>=N or ny>=M:
        continue

      if graph[nx][ny]==0 and visited[nx][ny][crash]==0:
        queue.append((nx,ny,crash))
        visited[nx][ny][crash] = visited[x][y][crash]+1

      if graph[nx][ny]==1 and crash==0:
        queue.append((nx,ny,crash+1))
        visited[nx][ny][crash+1] = visited[x][y][crash]+1

  return -1
  
print(bfs(0,0,0,visited))

    
    
  
