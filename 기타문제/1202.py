import sys
import heapq

N,K = map(int,sys.stdin.readline().split())

product = []
bag = []
heap = []

for _ in range(N):
  M,V = map(int,sys.stdin.readline().split())
  heapq.heappush(product, [M,-V])

for _ in range(K):
  heapq.heappush(bag,int(sys.stdin.readline()))
  
answer = 0

for _ in range(K):
  z = heapq.heappop(bag)

  while product and z>=product[0][0]:
    heapq.heappush(heap, heapq.heappop(product)[1])
  
  if heap:
    answer -= heapq.heappop(heap)
  
  elif not product:
    break
     
print(answer)


