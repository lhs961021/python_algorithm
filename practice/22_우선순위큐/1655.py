import sys
import heapq

N = int(sys.stdin.readline())

g_left = []
g_right = []
answer = []

for i in range(N):
  a = int(sys.stdin.readline())

  if len(g_left)==len(g_right):
    heapq.heappush(g_left,(-a,a))
  else:
    heapq.heappush(g_right,(a,a))
  
  if g_right and g_left[0][1]>g_right[0][0]:
    min=heapq.heappop(g_right)[0]
    max=heapq.heappop(g_left)[1]

    heapq.heappush(g_left,(-min,min))
    heapq.heappush(g_right,(max,max))

  answer.append(g_left[0][1])

for i in answer:
  print(i)
  
# 구글링