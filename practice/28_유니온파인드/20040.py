import sys
from collections import Counter 

n,m = map(int,sys.stdin.readline().split())

parent=[i for i in range(n+1)]

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a<b:
    parent[b]=a
  else:
    parent[a]=b

answer = 0

for i in range(1,m+1):
  a,b = map(int,sys.stdin.readline().split())
  if find_parent(parent,a)==find_parent(parent,b) and answer==0:
    answer = i
    break
  union_parent(parent,a,b)
  
print(answer)
  