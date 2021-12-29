import sys

x = int(input())

for _ in range(x):
  H, M, N= map(int, sys.stdin.readline().split())
  x = N//H
  y = N%H
  if y!=0:
    x = x+1
    if x<10:
      print(str(y)+"0"+str(x))
    else:
      print(str(y)+str(x))
  else:
    if x<10:
      print(str(H)+"0"+str(x))
    else:
      print(str(H)+str(x))


  


    
