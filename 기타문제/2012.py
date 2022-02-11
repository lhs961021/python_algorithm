import sys

N = int(sys.stdin.readline())

answer = [i for i in range(1,N+1)]

graph = []

for _ in range(N):
  graph.append(int(sys.stdin.readline()))

graph.sort()

x = 0

for i in range(N):
  x += abs(answer[i]-graph[i])

print(x)