import sys

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

data.sort()

answer=0
sum_1 = 0

for i in range(N-1,-1,-1):
  sum_1=0
  for j in range(0,i+1):
    sum_1 += data[j]
  answer += sum_1

print(answer)
