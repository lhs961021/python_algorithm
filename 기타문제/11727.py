import sys

n = int(sys.stdin.readline())

d = [0] * (n+1)
d[1] = 1
d[2] = 3

if n==1:
  print(d[1])
elif n==2:
  print(d[2])
else:
  for i in range(3,n+1):
    d[i] = d[i-1]+2*d[i-2]

  print(d[i]%10007) 