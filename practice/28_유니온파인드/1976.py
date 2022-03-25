import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [i for i in range(N+1)]

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

for i in range(1,N+1):
  graph = list(map(int,sys.stdin.readline().split()))

  for j in range(N):
    if graph[j] == 1:
      union_parent(parent,i,j+1)

answer = list(map(int,sys.stdin.readline().split()))

for i in range(len(answer)-1):
  if parent[answer[i]] == parent[answer[i+1]]:
    pass
  else:
    print("NO")
    break

  if i==len(answer)-2:
    print("YES")
    
    

