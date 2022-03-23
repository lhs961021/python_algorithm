import sys

n = int(sys.stdin.readline())

graph = []
d = [0]*10001


for _ in range(n):
  graph.append(int(sys.stdin.readline()))


for i in range(n):
  if i==0:
    d[0]=graph[0]
  elif i==1:
    d[1]=graph[0]+graph[1]
  elif i==2:
    d[2]=max(d[1],graph[0]+graph[2],graph[1]+graph[2])
  else:
    d[i]=max(d[i-1],d[i-2]+graph[i],d[i-3]+graph[i-1]+graph[i])

print(d[n-1])