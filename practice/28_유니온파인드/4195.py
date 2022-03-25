import sys

T = int(sys.stdin.readline())

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a!=b:
    parent[b]=a
    number[a] += number[b]

for _ in range(T):
  F = int(sys.stdin.readline())

  parent = {}
  number = {}

  for _ in range(F):
    f,r = map(str,sys.stdin.readline().split())

    if f not in parent:
      parent[f]=f
      number[f]=1
    if r not in parent:
      parent[r]=r
      number[r]=1

    union_parent(parent,f,r)
    print(number[find_parent(parent,f)])

  
    

  