import sys

n,x = map(int,input().split())

data = []*n

data = list(map(int,sys.stdin.readline().split()))

for i in data:
  if i<x:
    print(i,end=" ")