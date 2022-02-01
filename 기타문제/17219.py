import sys

N, M = map(int,sys.stdin.readline().split())

graph = {}

for _ in range(N):
  a,b = map(str,sys.stdin.readline().split())
  graph[a]=b

for _ in range(M):
  print(graph[input().rstrip()])