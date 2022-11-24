import sys
INF = int(1e9)

N,M = map(int,sys.stdin.readline().split())

graph = [[]*(N+1) for _ in range(N+1)]

graph = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1,N+1):
  for b in range(1,N+1):
    if a==b:
      graph[a][b] = 0

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1,N+1):
  for a in range(1,N+1):
    for b in range(1,N+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

answer = INF
num = 0

for i in range(1,N+1):
  result = 0
  for j in range(1,N+1):
    if i!=j:
      result += graph[i][j]

  if result<answer:
    answer = result
    num = i

print(num)