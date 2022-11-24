import sys

N,K = map(int,sys.stdin.readline().split())

l = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

d = [0]*(K+1)

for w,v in l:
  for i in range(K,-1,-1):
    if i<w:
      break
    d[i] = max(d[i-w]+v, d[i])

print(d[K])