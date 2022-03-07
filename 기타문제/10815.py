import sys

N = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

answer = list(map(int,sys.stdin.readline().split()))

graph.sort()

def binary_search(graph,target):
  start = 0
  end = N-1
  
  while start<=end:
    mid = (start+end)//2

    if graph[mid]==target:
      return 1
      
    elif graph[mid]<target:
      start = mid+1
    
    else:
      end=mid-1
      
  return 0

for i in answer:
  print(binary_search(graph, i),end=" ")