
sum = 0
count = 0
semi = 2


N = int(input())
for _ in range(N):
  data = str(input())
  a = list(data)
  b = a[0]

  for i in a:
    if i=='O':
      if (i==b)&(count!=0):
        sum+=semi
        semi+=1
        b = i
      else:
        sum+=1
        b = i
    else:
      b = i
      semi = 2
    count += 1
  print(sum)
  
  semi = 2
  sum = 0
  count = 0


