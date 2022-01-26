import sys
import heapq


T = int(sys.stdin.readline())

for _ in range(T):
  K = int(sys.stdin.readline())
  
  graph = list(map(int,sys.stdin.readline().split()))

  an = 0
  q = []

  for i in graph:
    heapq.heappush(q,i)

  while len(q) > 1:
    
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    an += a + b

    heapq.heappush(q,a+b)

  print(an)