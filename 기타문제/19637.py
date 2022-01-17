import sys

N,M = map(int, sys.stdin.readline().split())

graph = []

for i in range(N):
  a,b = list(map(str, sys.stdin.readline().split()))
  graph.append([a,int(b)])
  if i==N-1:
    z = int(b)

graph.sort(key= lambda x : x[1])



def p(n):
  start = 0
  end = N-1
  result = 0

  while start<=end:
    mid = (start+end)//2

    if graph[mid][1] >= n:
      end = mid - 1
      result = mid

    else:
      start = mid+1
  
  return graph[result][0]
      
for _ in range(M):
  n = int(sys.stdin.readline())
  print(p(n))