import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
  a = int(sys.stdin.readline())
  data.append(a)

z = sorted(data)

for i in range(N):
  print(z[i])