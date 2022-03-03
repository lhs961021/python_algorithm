import sys

graph = []

for _ in range(3):
  graph.append(list(map(int,sys.stdin.readline().split())))

x1,y1 = graph[0]
x2,y2 = graph[1]
x3,y3 = graph[2]

S = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)

if S>0:
  print(1)
elif S==0:
  print(0)
else:
  print(-1)