import sys

N = int(sys.stdin.readline())

z = list(map(int,sys.stdin.readline().split()))

one = min(z)
two = min([z[0]+z[1],
      z[0]+z[2],
      z[0]+z[3],
      z[0]+z[4],
      z[1]+z[2],
      z[2]+z[4],
      z[3]+z[4],
      z[1]+z[3],
      z[5]+z[1],
      z[5]+z[3],
      z[5]+z[2],
      z[5]+z[4]])
three = min([z[0]+z[1]+z[2],
      z[0]+z[1]+z[3],
      z[0]+z[3]+z[4],
      z[0]+z[2]+z[4],
      z[5]+z[1]+z[2],
      z[5]+z[1]+z[3],
      z[5]+z[3]+z[4],
      z[5]+z[2]+z[4]])

answer = 0

if N==1:
  z.sort()
  print(sum(z)-z[5])
else:
  answer = (4*three)+((4*(2*N-3))*two)+((((N-2)**2)+((N-2)*(N-1)*4))*one)

  print(answer)