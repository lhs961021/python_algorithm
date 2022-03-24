import sys

N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

start, end = 1, K

while start<=end:
  mid = (start+end)//2

  count = 0

  for i in range(1,N+1):
    count += min(mid//i,N)

  if count >= K:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)

# 이게 왜 성립하는지 모르겠다..