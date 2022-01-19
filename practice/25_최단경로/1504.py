import sys
import heapq

INF = int(1e9)

N,E = map(int,sys.stdin.readline().split())

graph = [[] for i in range(N+1)]

for _ in range(E):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

l,m = map(int, sys.stdin.readline().split())

def dji(start):
  distance = [INF]*(N+1)
  distance[start] = 0
  q = []
  heapq.heappush(q,(0,start))
  
  while q:
    dist, now = heapq.heappop(q)

    if distance[now]<dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost<distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  
  return distance

j = dji(1)
k = dji(l)
z = dji(m)

cnt = min(j[l]+k[m]+z[N],j[m]+z[l]+k[N])

if cnt<INF:
  print(cnt)
else:
  print(-1)