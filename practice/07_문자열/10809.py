N = str(input())

data = list(N)

for i in range(97,123):
  b = chr(i)
  a = data.count(b)
  if a==0:
    print(-1,end=" ")
  else:
    print(data.index(b),end=" ")