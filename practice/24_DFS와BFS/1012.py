import sys

N = int(sys.stdin.readline())

sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x<0 or y<0 or x>N-1 or y>M-1:
      return False
    if graph[x][y]==1:
      graph[x][y]+=1
      dfs(x-1,y)
      dfs(x,y-1)
      dfs(x+1,y)
      dfs(x,y+1)
      return True
    return False

for _ in range(N):
  M,N,K = map(int,sys.stdin.readline().split())

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x,y = map(int,sys.stdin.readline().split())
    graph[y][x] = 1

  result = 0

  for i in range(N):
    for j in range(M):
      if dfs(i,j)==True:
        result+=1
  print(result)

#python 에서는 재귀가 제한되어있으므로 sys.setrecursionlimit(10**6)을 써주어야함