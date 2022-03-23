import sys

INF = int(1e9)

V,E = map(int,sys.stdin.readline().split())

visited = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
  a,b,c = map(int,sys.stdin.readline().split())
  visited[a][b]=c

for i in range(1,V+1):
  visited[i][i]=INF

for k in range(1,V+1):
  for a in range(1,V+1):
    for b in range(1,V+1):
      visited[a][b] = min(visited[a][b],visited[a][k]+visited[k][b])

answer = INF

for i in range(1,V):
  for j in range(i,V+1):
    answer = min(answer,visited[i][j]+visited[j][i])

if answer==INF:
  print(-1)
else:
  print(answer)