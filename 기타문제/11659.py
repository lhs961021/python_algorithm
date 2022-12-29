import sys

N,M = map(int,sys.stdin.readline().split())

l = list(map(int,sys.stdin.readline().split()))

for i in range(1,N):
  l[i] = l[i]+l[i-1]

for _ in range(M):
  i,j = map(int,sys.stdin.readline().split())
  if i==1:
    print(l[j-1])
  elif i==j:
    print(l[i-1]-l[i-2])
  else:
    print(l[j-1]-l[i-2])