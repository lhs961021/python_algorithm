import sys

T = int(sys.stdin.readline())

def bfs(x):
  queue = [x]
  visited[x] = 1
  cnt = 0
  while queue:
    now = queue.pop()
    for nx in graph[now]:
      if visited[nx]==0:
        visited[nx]=1
        cnt += 1
        queue.append(nx)
  return cnt


for _ in range(T):
  N,M = map(int,sys.stdin.readline().split())
  visited = [False]*(N+1)
  graph = [[] for _ in range(N+1)]

  for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

  answer = 0

  for i in range(1,N+1):
    if visited[i]==0:
      answer += bfs(i) 
  print(answer)