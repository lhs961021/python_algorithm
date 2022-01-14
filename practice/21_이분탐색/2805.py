import sys

N,M = map(int,sys.stdin.readline().split())

graph = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(graph)
result = 0

while start<=end:
  
  answer = []
  mid = (start+end)//2
  
  answer = [i-mid for i in graph if i >= mid]
  a = sum(answer)

  if a<M:
    end = mid -1
  else:
    result = mid
    start = mid + 1

print(result)