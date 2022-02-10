import sys

N, M = map(int,sys.stdin.readline().split())

a = []

for _ in range(M):
  a.append(list(map(int,sys.stdin.readline().split())))


b = sorted(a,key=lambda a:a[1])

a.sort()


if a[0][0]==0 or a[0][1]==0 or b[0][0]==0 or b[0][1]==0:
    print(0)
else:
  if N<=6:
    if a[0][0] <= (b[0][1])*N:
      print(a[0][0])
    else:
      print((b[0][1])*N)
  else:
    answer = a[0][0] * (N//6)
    if answer >= (b[0][1])*N:
      print((b[0][1])*N)
    else:
      z = N % 6
      if a[0][0] <= (b[0][1])*z:
        print(answer+a[0][0])
      else:
        print(answer+(b[0][1])*z)


  