import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
  heapq.heappush(heap, int(sys.stdin.readline()))

answer = 0

if N==1:
  print(0)
elif N==2:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  print(a+b)
else:
  while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += (a+b)
    heapq.heappush(heap, (a+b))
  print(answer)

  
  