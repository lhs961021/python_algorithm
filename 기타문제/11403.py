import sys

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

for k in range(n):
  for a in range(n):
    for b in range(n):
      if graph[a][k] and graph[k][b]:
        graph[a][b] = 1

for i in graph:
  print(*i)
      