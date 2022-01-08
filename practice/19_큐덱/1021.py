import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

data = deque(i for i in range(1,N+1))

answer = list(map(int,sys.stdin.readline().split()))

count = 0
popin = []

z=1

for i in range(M):
  z = 1
  while z==1:
    if data[0]==answer[i]:
      popin.append(data[0])
      data.popleft()
      z = 0
    else:
      if data.index(answer[i])<=int(len(data)/2):
        data.rotate(-1)
        count += 1
      else:
        data.rotate(1)
        count += 1
    
print(count)
  