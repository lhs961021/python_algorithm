import sys
from collections import deque

M,N,H = map(int,sys.stdin.readline().split())

graph = []

queue = deque()

for i in range(H):
  tmp = []
  for j in range (N):
    tmp.append(list(map(int, sys.stdin.readline().split())))
    for k in range(M):
      if tmp[j][k]==1:
        queue.append((i,j,k))
  graph.append(tmp)


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():

  while queue:
    x,y,z = queue.popleft()

    for i in range(6):
      nx = dx[i]+x
      ny = dy[i]+y
      nz = dz[i]+z
      if nx<0 or ny<0 or nz<0 or nx>H-1 or ny>N-1 or nz>M-1:
        continue
      if graph[nx][ny][nz]==0:
        queue.append((nx,ny,nz))
        graph[nx][ny][nz] = graph[x][y][z] + 1
        
bfs()

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
              print(-1)
              exit(0)
        day = max(day,max(j))
print(day-1)