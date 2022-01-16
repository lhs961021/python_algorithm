import sys
from itertools import combinations

N,M = map(int, sys.stdin.readline().split())

graph = [i for i in range(1,N+1)]
  
for i in list(combinations(graph,M)):
  for j in range(M):
    print(i[j],end =" ")
  print("")
