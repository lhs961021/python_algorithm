import sys

N,M,B = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

time = 9223372036854775807

for i in range(257):
  top = 0
  bottom = 0
  target = i
  for j in range(N):
    for k in range(M):
      if graph[j][k]>=i:
        top += graph[j][k] - i
      else:
        bottom += i-graph[j][k]
  if bottom > top+B:
    continue
  else:
    t = bottom + top*2
    if t<=time:
      time = t
      height = i
print(time,height)

