import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

result = []

for _ in range(M):
  A,B = map(int,sys.stdin.readline().split())
  graph[B].append(A)

def bfs(start):
  count = 1
  visited = [0 for _ in range(N+1)]
  visited[start] = 1
  queue = deque([start])
  
  while queue:
    a = queue.popleft()

    for v in graph[a]:
      if not visited[v]:
        queue.append(v)
        visited[v] = 1
        count += 1
        
  return count

answer = 0

for i in range(1,N+1):
  z = bfs(i)
  if answer<z:
    answer = z
  result.append([z,i])
  
for i in result:
  if i[0]==answer:
    print(i[1],end=" ")

  
    