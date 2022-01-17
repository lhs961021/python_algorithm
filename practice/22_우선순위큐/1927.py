import sys
import heapq

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  a = int(sys.stdin.readline())
  if a!=0:
    heapq.heappush(graph,a)
  elif a==0:
    if len(graph)!=0:
      print(heapq.heappop(graph))
    else:
      print(0)
  

