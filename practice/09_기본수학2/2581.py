
N = int(input())
X = int(input())


sum = 0
z=0

for i in range(N,X+1):
  if i==1:
    pass
  elif i==2:
    sum += i
    z = i
  else:
    for j in range(2,i):
      m = i / j 
      if m==int(m):
        break
      else:
        if j==(i-1):
          sum += i
          if z==0:
            z = i


if (sum==0):
  print(-1)
else:
  print(sum)
  print(z)

  