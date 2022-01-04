import sys

N = int(input())

stk = []

for _ in range(N):
  A = int(sys.stdin.readline())
  if A==0:
    stk.pop()
  else:
    stk.append(A)

print(sum(stk))
