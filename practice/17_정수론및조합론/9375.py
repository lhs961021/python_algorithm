import sys
from collections import Counter

N = int(input())
for _ in range(N):  
  z = int(sys.stdin.readline())
  data = []
  answer = 1 
  for _ in range(z):
    k, n = map(str, sys.stdin.readline().split())
    data.append(n)

  a = Counter(data)

  for i in a.values():
    answer *= (i+1)

  print(answer-1)




