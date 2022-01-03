import sys

N = int(sys.stdin.readline())

answer = []
data = []
C = 0

for _ in range(N):
  A,B = sys.stdin.readline().split()
  data.append([int(A),C,B])
  C+=1

answer = sorted(data)

for i in range(N):
  print(answer[i][0], end=" ")
  print(answer[i][2])