import sys

N,M = map(int,sys.stdin.readline().split())

graph = []
visited = [[False]*M for _ in range(N)] 

for _ in range (N):
  graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


def dfs(x,y):

  global flag
  visited[x][y]=True

  for i in range(8):
    nx = dx[i]+x
    ny = dy[i]+y

    if 0<=nx<N and 0<=ny<M:
  
      if graph[nx][ny]>graph[x][y]:
        flag = False
      
      if visited[nx][ny]==False and graph[nx][ny]==graph[x][y]:
        dfs(nx,ny)


result = 0

for i in range(N):
  for j in range(M):
    if graph[i][j]>0 and not visited[i][j]:
      flag = True
      dfs(i,j)
      if flag:
        result += 1

print(result)
