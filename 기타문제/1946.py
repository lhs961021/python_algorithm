import sys

T = int(sys.stdin.readline())

for _ in range(T):

  N = int(sys.stdin.readline())

  graph = []

  for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

  a0 = sorted(graph,key=lambda x:x[0])

  m1 = a0[0][1]

  most = 1

  for i in a0:
    if m1>i[1]:
      most += 1
      m1 = i[1]

  print(most)