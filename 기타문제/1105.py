import sys

L,R = map(int,sys.stdin.readline().split())

if len(str(L))!=len(str(R)):
  print(0)
else:
  count = 0
  L = list(str(L))
  R = list(str(R))

  if L[0]==R[0]:
    if L[0]=='8':
      count += 1

    for i in range(1,len(L)):
      if L[i]==R[i]:
        if L[i]=='8':
          count += 1
      else:
        break

    print(count)
  else:
    print(0)

