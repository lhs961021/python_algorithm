import sys

m,n = map(int, sys.stdin.readline().split())

sum = 1
sum_1 = 1
for i in range(m,m-n,-1):
  sum *= i
for j in range(1,n+1):
  sum_1 *= j

print(int(sum/sum_1))
