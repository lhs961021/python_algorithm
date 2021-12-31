import sys

while(1):
  x,y,z = map(int,sys.stdin.readline().split())

  if x==0 and y==0 and z==0:
    break

  a = max(x,y,z)
  c = min(x,y,z)

  for i in (x,y,z):
    if i!=a and i!=c:
      b=i
      break

  if (a*a)==((b*b)+(c*c)):
    print("right")
  else:
    print("wrong")

