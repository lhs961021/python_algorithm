import sys
import math

n = int(sys.stdin.readline())

data = []
stk = []
gcd = 0

for i in range(n):
  data.append(int(input()))
  if i == 1:
    gcd = abs(data[1] - data[0])
  gcd = math.gcd(abs(data[i] - data[i - 1]), gcd)

k = int(gcd ** 0.5)

for i in range(2,k+1):
  if gcd%i==0:
    stk.append(i)
    stk.append(gcd//i)
stk.append(gcd)
stk = list(set(stk))
stk.sort()

print(*stk)

#그냥 구글링