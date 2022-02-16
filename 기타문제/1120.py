import sys

a,b = map(str,sys.stdin.readline().split())

a1 = list(a)
b1 = list(b)

z = len(b1)-len(a1)


graph = []
for i in range(0,z+1):
  a = 0
  for j in range(len(a1)):
    if a1[j]!=b1[j+i]:
      a+=1
  graph.append(a)

print(min(graph))

  