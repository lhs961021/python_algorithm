import sys

N = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

answer = list(map(int,sys.stdin.readline().split()))

a = sorted(answer)

count = [0]*20000001

def binary_search(target,start,end):

  while start<=end:

    mid = (start+end)//2
    
    if target==a[mid]:
      count[a[mid]-1] += 1
      return

    elif target > a[mid]:
      start = mid + 1

    else:
      end = mid - 1

  return 

for i in range(N):
  target = graph[i]
  binary_search(target,0,M-1)

for i in answer:
  print(count[i-1],end=" ")
