import sys

m = list(map(int,sys.stdin.readline().split()))

sum = 0

for i in range(len(m)):
  sum += (m[i]*m[i])

print(sum%10)