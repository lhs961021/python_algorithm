import sys
import heapq
from collections import deque

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

start,end = map(int,sys.stdin.readline().split())
queue = deque([start])
path = [[] for _ in range(N+1)]
path[start].append(start)

def dijkstra(start,queue):
  q = []

  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))
        path[i[0]] = []
        for k in path[now]:
          path[i[0]].append(k)
        path[i[0]].append(i[0])
        
dijkstra(start,queue)

print(distance[end])
print(len(path[end]))
print(* path[end])