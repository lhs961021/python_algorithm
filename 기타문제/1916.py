import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

x,y = map(int,sys.stdin.readline().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(x)
  
print(distance[y])