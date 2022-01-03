import sys
from collections import Counter

N = int(sys.stdin.readline())


data = []

for _ in range(N):
  a = int(sys.stdin.readline())
  data.append(a)

z = sorted(data)

l = Counter(z).most_common(2)

if len(l)==1:
  c = l[0][0]
else:
  if l[0][1]==l[1][1]:
    c = l[1][0]
  else:
    c = l[0][0]

a = round(sum(z)/N)
b = z[int((N-1)/2)]
d = z[N-1]-z[0]

print(a)
print(b)
print(c)
print(d)