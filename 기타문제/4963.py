import sys

sys.setrecursionlimit(100000)

def dfs(x,y):
  
  if x<0 or y<0 or x>h-1 or y>w-1:
    return False
  
  if graph[x][y]==1:
    graph[x][y]=0
    for i in range(8):
      nx = dx[i]+x
      ny = dy[i]+y
      dfs(nx,ny)
    return True
  return False

while 1:
  w,h = map(int,sys.stdin.readline().split())
  
  if w==0 and h==0:
    quit()
  else:
    graph=[]
  
    for _ in range(h):
      graph.append(list(map(int,sys.stdin.readline().split())))
  
    count = 0

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,1,-1,1,-1]

    for i in range(h):
      for j in range(w):
        if dfs(i,j)==True:
          count += 1
  
    print(count)