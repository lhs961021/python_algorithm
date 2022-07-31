import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = str(sys.stdin.readline())

answer = 0
count = 0
i = 0

while (i<=M-1):
  if S[i:i+3]=='IOI':
    count += 1
    if count == N:
      count -= 1
      answer += 1
    i += 2
  else:
    count = 0
    i += 1

print(answer)