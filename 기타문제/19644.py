import sys
from collections import deque

L = int(sys.stdin.readline())
Ml,Mk = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())

q = deque()
j = deque()

for _ in range(L):
  q.append(int(sys.stdin.readline()))

count = 1
z = 0
l = 0
p = 0
k = 0
mom = 0

while q:

  a = q.popleft()
  l += 1

  if l-Ml>=0:

    if j:
      mom = j.pop()
      if l-mom<=Ml:
        k = l
        p += 1

    if l-mom <= Ml:
      count = Ml - p
    else:
      count = Ml
    
    if a<=Mk*(count):
      continue
    else:
      if C>0:
        C -= 1
        j.append(l)
        continue
      else:
        print("NO")
        z = 1
        break

  else:
    if a<=Mk*(count):
      count += 1
      continue
    else:
      if C>0:
        C -= 1
        j.append(l)
        continue
      else:
        print("NO")
        z = 1
        break

if z==0:
  print("YES")