import sys

N = int(sys.stdin.readline())

d = [0]*41

def fibonacci(n):
  if n == 0:
    return d[n]
  if n==1:
    d[n] = 1
    return d[n]
  if d[n]!=0:
    return d[n]
 
  d[n] = fibonacci(n-1)+fibonacci(n-2)

  return d[n]

for _ in range(N):
  a = int(sys.stdin.readline())
  if a==0:
    print(1,0)
  else:
    print(fibonacci(a-1),fibonacci(a))






