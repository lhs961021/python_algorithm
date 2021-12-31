import sys

data =[]

x1,y1 = map(int,sys.stdin.readline().split())
x2,y2 = map(int,sys.stdin.readline().split())
x3,y3 = map(int,sys.stdin.readline().split())  

if x1==x2:
  if y1==y3:
    print(x3,end=" ")
    print(y2)
  else:
    print(x3,end=" ")
    print(y1)
elif x1==x3:
  if y1==y2:
    print(x2,end=" ")
    print(y3)
  else:
    print(x2,end=" ")
    print(y1)
else:
  if y1==y3:
    print(x1,end=" ")
    print(y2)
  else:
    print(x1,end=" ")
    print(y3)