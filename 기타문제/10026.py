import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  l = list(sys.stdin.readline().rstrip())
  graph.append(l)

visited = [[False]*(N) for _ in range(N)]

def dfs(x,y):
  visited[x][y] = True
  flag = graph[x][y]

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
 
    if (0<=nx<N) and (0<=ny<N):
      if visited[nx][ny]==False:
        if graph[nx][ny] == flag:
          dfs(nx,ny)

count = 0

for i in range(N):
  for j in range(N):
    if visited[i][j]==False:
      dfs(i,j)
      count += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if graph[i][j]=='G':
      graph[i][j]='R'

count_two = 0
for i in range(N):
  for j in range(N):
    if visited[i][j]==False:
      dfs(i,j)
      count_two += 1

print(count,count_two)