import sys

A,B,C= map(int, sys.stdin.readline().split())

k = (C-B)/(A-B)

if k == int(k):
  print(int(k))
else:
  print(int(k)+1)
  
#문제풀이 헷갈려서 구글 참조