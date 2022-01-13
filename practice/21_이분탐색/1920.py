import sys

N = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))

graph.sort()

M = int(sys.stdin.readline())

answer = list(map(int,sys.stdin.readline().split()))

def binary_search(target,start,end):

  while start<=end:

    mid = (start+end)//2
    
    if target==graph[mid]:
      print(1)
      return

    elif target > graph[mid]:
      start = mid + 1

    else:
      end = mid - 1

  print(0)
  return 

for i in range(M):
  target = answer[i]
  binary_search(target,0,N-1)
  
