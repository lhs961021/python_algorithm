import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())

graph = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m = 0

for _ in range(N):
  l = list(map(int,sys.stdin.readline().split()))
  m = max(m,max(l))
  graph.append(l)

length = len(graph)

def dfs(x,y,h):

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<length and 0<=ny<length and visited[nx][ny]==False and graph[nx][ny] > h:
      visited[nx][ny]=True
      dfs(nx,ny,h)

result = 1

for k in range(1,m+1):
  visited = [[False]*length for _ in range(length)]
  count = 0
  for i in range(length):
    for j in range(length):
      if graph[i][j] > k and visited[i][j]==False:
        count += 1
        visited[i][j] = True
        dfs(i,j,k)

  result = max(result,count)
  
print(result)