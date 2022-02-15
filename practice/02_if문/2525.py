import sys

a,b = map(int,sys.stdin.readline().split())

c = int(sys.stdin.readline())

d = (b+c) // 60

if b+c > 59:
  a = a + d
  c = b+c - (d*60) 
  if a >= 24:
    a = a-24
    print(a,c)
  else:
    print(a,c)
else:
  b = b+c
  print(a,b)