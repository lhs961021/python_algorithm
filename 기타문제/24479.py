import sys
sys.setrecursionlimit(10**7)

N,M,R = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort(reverse=True)

count = 1

answer = [0]*(N)
visited = [False]*(N+1)

def dfs(R,answer):
  stack = [R]
  count = 1
  
  while(stack):
    node = stack.pop()
    
    if visited[node]==False:
      visited[node]=True
      answer[node-1]=count
      count += 1
      stack.extend(graph[node])
    
  return answer

dfs(R,answer)

for i in answer:
  print(i)