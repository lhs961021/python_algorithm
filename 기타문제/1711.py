import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

count = 0

for i in range(N):
  x1,y1 = graph[i]
  for j in range(i+1,N):
    x2,y2 = graph[j]
    for k in range(j+1,N):
      
      x3,y3 = graph[k]
      a = (((x1-x2)**2)+((y1-y2)**2))
      b = (((x2-x3)**2)+((y2-y3)**2))
      c = (((x1-x3)**2)+((y1-y3)**2))
      
      if a==b+c or b==a+c or c==a+b:
        count +=1

print(count)