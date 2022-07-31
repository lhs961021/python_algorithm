import sys
from collections import deque

sys.setrecursionlimit(10**7)

N,M,R = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort()

visited = [False]*(N+1)

answer = [0]*(N)

def bfs(R,answer):
  visited[R]=True
  count = 1
  answer[R-1]=count
  queue = deque([R])
  count += 1

  while queue:
    node = queue.popleft()
    
    for i in graph[node]:
      if visited[i]==False:
        visited[i]=True
        answer[i-1]=count
        count += 1
        queue.append(i)

  return answer

bfs(R,answer)

for i in answer:
  print(i)