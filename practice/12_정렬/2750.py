N = int(input())

data = []

for _ in range(N):
  a = int(input())
  data.append(a)

z = sorted(data)

for i in range(N):
  print(z[i])