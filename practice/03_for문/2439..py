T = int(input())


for i in range(1,T+1):
  for _ in range(T,i,-1):
    print(" ",end='')
  for _ in range(i):
    print("*",end='')
  print()
  