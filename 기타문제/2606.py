import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False]*(N+1)

queue = deque([1])
answer = 0

while queue:
  start = queue.pop()

  if visited[start]==False:
    visited[start] = True
    queue.extend(graph[start])
    answer+=1

print(answer-1)