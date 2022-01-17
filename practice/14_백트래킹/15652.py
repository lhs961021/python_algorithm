import sys
from itertools import combinations_with_replacement

N,M = map(int,sys.stdin.readline().split())

graph = [i for i in range(1,N+1)]

a = list(combinations_with_replacement(graph,M))

for i in a:
  for j in i:
    print(j,end=" ")
  print()
