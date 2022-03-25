import sys

sys.setrecursionlimit(10**5)

n,m = map(int,sys.stdin.readline().split())

parent = [i for i in range(n+1)]

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



for _ in range(m):
  z,k,l = map(int,sys.stdin.readline().split())
  if z==0:
    union_parent(parent,k,l)
  else:
    answer = False
    if find_parent(parent,k)==find_parent(parent,l):
      answer = True

    if answer==True:
      print("yes")
    else:
      print("no")
      
      
    