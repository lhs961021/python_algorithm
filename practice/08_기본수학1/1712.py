import sys

A,B,C = map(int, sys.stdin.readline().split())

try:
  x = float(A / (C - B))

  if x<0:
    print(-1)
  else:
    print(int(x+1))
except:
  print(-1)