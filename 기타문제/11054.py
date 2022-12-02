import sys

N = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))
k = l[::-1]
dp_increase = [1]*N
dp_decrease = [1]*N

flag = max(l)

for i in range(1,N):
  for j in range(0,i):
    if l[j]<l[i]:
      dp_increase[i] = max(dp_increase[i],dp_increase[j]+1)
    if k[j]<k[i]:
      dp_decrease[i] = max(dp_decrease[i],dp_decrease[j]+1)

result = 0

for i in range(N):
  result = max(result,dp_increase[i]+dp_decrease[N-i-1]-1)

print(result)