import sys

N,M = map(int,sys.stdin.readline().split())

graph = {}

for i in range(1,N+1):
  a = str(sys.stdin.readline().rstrip())
  graph[str(i)] = a
  graph[a] = str(i)
  

for _ in range(M):
  z = sys.stdin.readline().rstrip()
  print(graph[z])