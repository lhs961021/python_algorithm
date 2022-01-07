import sys
from collections import deque

answer = []

N,K = map(int,sys.stdin.readline().split())

data = deque(i for i in range (1,N+1))

while len(data)!=0:
  data.rotate(-(K-1))
  a = data[0]
  data.remove(data[0])
  answer.append(a)
  

print("<",end="")
for i in range (len(answer)):
  if i==len(answer)-1:
    print(answer[i],end="")
  else:
    print(answer[i],end=", ")
print(">")
