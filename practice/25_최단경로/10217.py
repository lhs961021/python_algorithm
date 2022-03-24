import sys
from collections import deque

INF = int(1e9)

T = int(sys.stdin.readline())

def dijkstra(start):
  queue = deque()
  queue.append((start,0,0))
  distance[1][0] = 0

  while queue:
    now,cost,dist = queue.popleft()

    if distance[now][cost]<dist:
      continue

    for city,c,d in graph[now]:
      r_cost = c + cost
      r_dist = d + dist

      if r_cost<=M and r_dist<distance[city][r_cost]:
        for i in range(r_cost,M+1):
          if r_dist<distance[city][i]:
            distance[city][i] = r_dist
          else:
            break
        queue.append((city,r_cost,r_dist))

  return distance[N][M]

for _ in range(T):
  N,M,K = map(int,sys.stdin.readline().split())

  graph = [[] for _ in range(N+1)]

  for _ in range(K):
    u,v,c,d = map(int,sys.stdin.readline().split())
    graph[u].append((v,c,d))


  distance = [[INF]*(M+1) for _ in range(N+1)]
  
  answer = dijkstra(1)
  
  if answer!=INF:
    print(answer)
  else:
    print("Poor KCM")
  