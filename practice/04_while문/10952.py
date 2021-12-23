import sys

while (1):
  A,B = map(int,sys.stdin.readline().split())
  C = A+B
  if C==0:
    break
  else:
    print(C)
