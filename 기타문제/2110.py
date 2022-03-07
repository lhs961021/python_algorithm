import sys

N,C = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
  graph.append(int(sys.stdin.readline()))

graph.sort()

start = 1 #거리의 최솟값
end = graph[N-1]-graph[0] #거리의 최댓값

result = 0 #정답

while start<=end:
  mid = (start+end)//2 #거리의 중간값
  pin = graph[0] # 첫번째 공유기 설치
  count = 1

  for i in range(1,N): # 1부터 끝까지 
    if graph[i] >= pin+mid: # 만약 그래프의 그 지점이 거리의 중간값+첫번째 공유기 설치값보다 크거나 같으면 
      count += 1
      pin = graph[i]

  if count >= C:
    start = mid + 1
    result = mid
  else:
    end = mid -1

print(result)

  
  