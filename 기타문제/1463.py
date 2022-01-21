import sys

N = int(sys.stdin.readline())

d = [0]*1000001

for i in range(2,N+1):

  d[i] = d[i-1]+1

  if i%3==0:
    d[i] = min(d[i],d[int(i/3)]+1)
  
  if i%2==0:
    d[i] = min(d[i],d[int(i/2)]+1)
  
print(d[N])
   