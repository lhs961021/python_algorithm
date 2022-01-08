import sys

N,K = map(int,sys.stdin.readline().split())

data = []

for _ in range(N):
  n = int(sys.stdin.readline())
  if n<=K:
    data.append(n)

count = 0

a = len(data)


for i in range(a-1,-1,-1):
  while K>=data[i]:
    m = K//data[i]
    count += m
    K = K - (m*data[i])
  if K==0:
    break

print(count)

  

