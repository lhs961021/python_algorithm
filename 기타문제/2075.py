import sys
import heapq

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
  if i == 0:
    heapq.heapify(graph[0])
  else:  
    for j in graph[i]:
      if graph[0][0]<j:
        heapq.heappop(graph[0])
        heapq.heappush(graph[0], j)

print(graph[0][0])
