import sys

K,N = map(int,sys.stdin.readline().split())

graph = []

for _ in range(K):
  graph.append(int(sys.stdin.readline()))

start = 1
end = max(graph)

result = 0
while start<=end:
  answer = 0

  mid = (start+end)//2

  for i in range(K):
    if graph[i]>=mid:
      answer += (graph[i]//mid)

  if answer<N:
    end = mid -1
  else:
    result = mid
    start = mid + 1

print(result)



  