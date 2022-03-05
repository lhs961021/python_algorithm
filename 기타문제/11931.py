import sys

N = int(sys.stdin.readline())

graph=[]

for _ in range(N):
  graph.append(int(sys.stdin.readline()))

graph.sort(reverse=True)

for i in graph:
  print(i)