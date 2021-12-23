N = int(input())

for _ in range(N):
  data = list(map(int, input().split()))
  a = data[0]
  df = 0
  sum = 0

  for i in data[1:]:
    sum += i

  avg = sum/a

  for i in data[1:]:
    if i>avg:
      df += 1

  m = df/a*100
  print(f'{m:.3f}%')