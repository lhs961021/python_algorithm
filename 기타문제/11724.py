import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
  u,v = map(int,sys.stdin.readline().split())
  graph[u].append(v)
  if u not in graph[v]:
    graph[v].append(u)



def bfs (graph,start,visited):
  answer = []
  visited[start] = True
  q = deque([start])
  while q:
    z = q.popleft()
    answer.append(z)
    for i in graph[z]:
      if visited[i]==False:
        q.append(i)
        visited[i]=True

  return tuple(answer)

pr = []

visited = [False]*(N+1)

for i in range(1,N+1):
  if visited[i]==True:
    continue
  pr.append(bfs(graph,i,visited))
 
print(len(set(pr)))