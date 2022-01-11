import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())

graph = []

for _ in range (N):
  graph.append(list(map(int, input().split())))

answer = []

queue = deque()
  
for i in range(N):
  for j in range(M):
    if graph[i][j]==1:
      queue.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
        
          

def bfs():
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y
      if nx<0 or ny<0 or nx>N-1 or ny>M-1:
        continue
      if graph[nx][ny] == 1:
        continue  
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))

bfs()

res = 0

for i in graph:
  for j in i:
    if j==0:
      print(-1)
      exit(0)
  res = max(res, max(i))  

print(res-1)