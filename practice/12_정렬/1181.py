import sys

N = int(sys.stdin.readline())

answer = []
data = []

for _ in range(N):
  A = sys.stdin.readline().rstrip()
  data.append(A)

z = list(set(data))

for i in range(len(z)):
  answer.append([len(z[i]),z[i]])

k = sorted(answer)

for i in range(len(k)):
  print(k[i][1])