a,b = map(list, input().split(" "))
z = int(a[2]+a[1]+a[0])
y = int(b[2]+b[1]+b[0])

if z>y:
  print(z)
else:
  print(y)