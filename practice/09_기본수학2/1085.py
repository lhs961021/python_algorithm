import sys

x,y,w,h = map(int,sys.stdin.readline().split())


a = (((x*x)+(y*y))**(1/2))
b = (((x*x)+((h-y)*(h-y)))**(1/2))
c = ((((w-x)*(w-x))+((h-y)*(h-y)))**(1/2))
d = ((((w-x)*(w-x))+(y*y))**(1/2))

z = min(a,b,c,d)

if z==a:
  if x>y:
    print(y)
  else:
    print(x)
elif z==b:
  if (h-y)>x:
    print(x)
  else:
    print(h-y)
elif z==c:
  if (h-y)>(w-x):
    print(w-x)
  else:
    print(h-y)
else:
  if y>(w-x):
    print(w-x)
  else:
    print(y)
