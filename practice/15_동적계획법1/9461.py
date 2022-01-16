import sys

N = int(sys.stdin.readline())

d = [0]*101

def P(n):
  if n==1 or n==2 or n==3:
    d[n]=1
    return 1
  if d[n]!=0:
    return d[n]
  d[n] = P(n-2)+P(n-3)

  return d[n]


for _ in range(N):
  a = int(sys.stdin.readline())
  print(P(a))
