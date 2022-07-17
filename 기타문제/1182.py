import sys
import itertools

n,s = map(int,sys.stdin.readline().split())

b = list(map(int,sys.stdin.readline().split()))
b.sort()

answer = 0

for i in range(1,n+1):
  z = list(itertools.combinations(b,i))
  for k in z:
    if sum(k)==s:
      answer += 1

print(answer)