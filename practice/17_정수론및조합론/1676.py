import sys
from math import factorial

N = int(sys.stdin.readline())

count = 0

a = factorial(N)

a = list(str(a))

for i in range(len(a)-1,-1,-1):
  if int(a[i])==0:
    count += 1
  else:
    break

print(count)



