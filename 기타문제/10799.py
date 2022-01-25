import sys

N = list(sys.stdin.readline().rstrip())

answer = 0
M = []
for i in range(len(N)):
  if N[i]=='(':
    M.append(N[i])
  else:
    if N[i-1]=='(':
      M.pop()
      answer += len(M)
    else:
      M.pop()
      answer += 1

print(answer)

