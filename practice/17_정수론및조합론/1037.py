import sys

N = int(sys.stdin.readline())

data = list(input().split())

for i in range (N):
  data[i] = int(data[i])

if len(data)==1:
  print(data[0]*data[0])
else:
  a = min(data)
  b = max(data)
  print(a*b)