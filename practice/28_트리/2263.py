import sys

sys.setrecursionlimit(200002)

n = int(sys.stdin.readline())

in_order = list(map(int,sys.stdin.readline().split()))
post_order = list(map(int,sys.stdin.readline().split()))

pos = [0]*(n+1)

for i in range(n):
  pos[in_order[i]]=i

def finder(in_start,in_end,post_start,post_end):
  
  if(in_start>in_end) or (post_start>post_end):
    return

  root = post_order[post_end]
  print(root,end=" ")

  left = pos[root] - in_start
  right = in_end - pos[root]

  finder(in_start,in_start+left-1,post_start,post_start+left-1)
  finder(in_end-right+1,in_end,post_end-right,post_end-1)
  
finder(0,n-1,0,n-1)
