import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    graph.append(int(sys.stdin.readline()))

d = [0]*301

d[0] = graph[0]
if N>=2:
    d[1] = graph[0]+graph[1]
if N>=3:
    d[2] = max(graph[0]+graph[2],graph[1]+graph[2])


for i in range(3,N):
    d[i] = max(d[i-3]+graph[i-1]+graph[i],d[i-2]+graph[i])

print(d[N-1])

