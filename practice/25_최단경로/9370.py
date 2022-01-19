import sys
import heapq
INF = int(1e9)


N = int(sys.stdin.readline())

def dji(s):
  q = []
  distance = [INF]*(n+1)
  distance[s] = 0
  heapq.heappush(q,(0,s))  

  while q:
    dist,now = heapq.heappop(q)

    if distance[now]<dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost<distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance

for _ in range(N):

  n,m,t = map(int,sys.stdin.readline().split())

  s,g,h = map(int,sys.stdin.readline().split())

  graph = [[] for i in range(n+1)]
    
  for _ in range(m):
    a,b,d = map(int,sys.stdin.readline().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

  s_=dji(s)
  g_=dji(g)
  h_=dji(h)

  answer = []

  for _ in range(t):
    f = int(sys.stdin.readline())
    if s_[g]+g_[h]+h_[f] == s_[f] or s_[h]+h_[g]+g_[f] == s_[f]:
      heapq.heappush(answer,f)

  for _ in range(len(answer)):
    print(heapq.heappop(answer),end=" ")
  print()


  









