import sys

A,B = map(int, sys.stdin.readline().split())
data = []*A
data = list(map(int,sys.stdin.readline().split()))

p = 1

for i in range(A):
  for j in range(i+1,A):
    for k in range(j+1,A):
      answer = data[i]+data[j]+data[k]
      if (answer<=B) and (answer>=p):
        p = answer

print(p)