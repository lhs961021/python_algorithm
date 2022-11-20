import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque()
queue.append((1,0))
count = 0
visited[1]=True

while queue:
  start,cost = queue.popleft()
  
  for i in graph[start]:
    if visited[i]==False:
      if cost<=1:
        count += 1
      visited[i] = True
      queue.append((i,cost+1))
  
print(count)
      

  