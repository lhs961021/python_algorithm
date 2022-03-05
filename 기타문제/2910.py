import sys
from collections import Counter


N,C = map(int,sys.stdin.readline().split())

graph = list(map(int,sys.stdin.readline().split()))

a = Counter(graph)
b = a.most_common()

for i in b:
  for _ in range(i[1]):
    print(i[0],end=" ")