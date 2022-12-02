import sys

N = int(sys.stdin.readline())

l = []

for _ in range(N):
  l.append(list(map(int,sys.stdin.readline().split())))

l.sort(key=lambda x:x[0])

dp = [1]*(N)

for i in range(1,N):
  for j in range(0,i):
    if l[i][1]>l[j][1]:
      dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))