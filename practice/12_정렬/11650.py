import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
  A,B = map(int, sys.stdin.readline().split())
  data.append([A,B])

m = sorted(data)

for i in range(N):
  print(m[i][0],end=" ")
  print(m[i][1])
