import sys

N = int(sys.stdin.readline())

data = []
answer = [1]*N

for i in range(N):
  A,B = map(int, sys.stdin.readline().split())
  data.append([A,B])

for i in range(N):
  for j in range(N):
    if i==j:
      continue
    if (data[i][0]>data[j][0]) and (data[i][1]>data[j][1]):
      answer[j] += 1

for i in answer:
  print(i,end=" ")


