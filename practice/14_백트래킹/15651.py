import sys
from itertools import product

N,M = map(int,sys.stdin.readline().split())

graph = [i for i in range(1,N+1)]

a = list(product(graph,repeat = M))

for i in a:
  for j in i:
    print(j,end=" ")
  print()
