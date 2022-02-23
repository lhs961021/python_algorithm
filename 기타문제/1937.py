import sys
sys.setrecursionlimit(300000)

n = int(sys.stdin.readline())

graph = []

answer = [[-1]*n for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):

  if answer[x][y]<0:
    answer[x][y]=1

    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y
  
      
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
  
      if graph[nx][ny]>graph[x][y]:
        answer[x][y] = max(answer[x][y],dfs(nx,ny)+1)
  
    return answer[x][y]
    
  else:
    return answer[x][y]

result = 0 

for i in range(n):
  for j in range(n):
    result = max(result,dfs(i,j))

print(result)

