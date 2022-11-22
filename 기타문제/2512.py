import sys

N = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))

budget = int(sys.stdin.readline())

result = 0
start = 0
end = max(graph)

while start <= end:
  total = 0
  mid = (start+end)//2
  
  for i in graph:
    if i > mid:
      total += mid
    else:
      total += i
      
  if total <= budget:
    start = mid + 1
    result = mid

  else:
    end = mid -1

print(result)