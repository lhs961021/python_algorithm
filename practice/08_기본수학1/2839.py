N = int(input())

b = N//3
breaker=False


for i in range(b,-1,-1):
  for j in range(b+1):
    k = i * 5
    p = j * 3
    if N==(k+p):
      breaker=True
      print(i+j)
      break
  if breaker==True:
    break

  if (i==0):
    print(-1)
    break


