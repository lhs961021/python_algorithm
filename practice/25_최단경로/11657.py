import sys

INF = int(1e9)

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

def bell():
  distance = [INF]*(N+1)
  distance[1] = 0
  for _ in range(N-1):
    for i in range(1,N+1):
      for v,c in graph[i]:
        if distance[i]==INF:
          continue
        if distance[v]> distance[i] + c:
          distance[v] = distance[i] + c

  for i in range(1,N+1):
    for a,b in graph[i]:
      if distance[i]==INF:
        continue
      if distance[a] > distance[i] + b:
        return False

  return distance 

distance = bell()

if distance==False:
  print(-1)
else:
  for i in range(2,N+1):
    if distance[i]<INF:
      print(distance[i])   
    else:
      print(-1)
      

  


 


