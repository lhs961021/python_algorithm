import sys

answer = []
sum_1 = 0

N = int(input())
data = list(map(int, sys.stdin.readline().split()))

M = max(data)

for i in data:
  a = i/M*100
  answer.append(a)


for i in answer:
  sum_1 += i

m = float(sum_1 / N)
print(m)
