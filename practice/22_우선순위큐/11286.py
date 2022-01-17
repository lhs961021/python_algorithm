import sys
import heapq

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  a = int(sys.stdin.readline())
  if a!=0:
    heapq.heappush(graph,[abs(a),a])
  elif a==0:
    if len(graph)!=0:
      a = heapq.heappop(graph)
      print(a[1])
    else:
      print(0)
  

