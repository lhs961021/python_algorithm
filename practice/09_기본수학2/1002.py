import sys

N = int(input())

for _ in range(N):
  x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())

  x = abs(x1-x2) 
  y = abs(y1-y2)

  d = ((x*x)+(y*y))**(1/2)

  if x==0 and y==0 and r1==r2:
    print(-1)
    continue

  if (r1+r2)<d:
    print(0)
  elif ((r1+r2)==d) or (abs(r1-r2))==d:
    print(1)
  else:
    if abs(r1-r2)>d and r1!=r2:
      print(0)
    else:
      print(2)




