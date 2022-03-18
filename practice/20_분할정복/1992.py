import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  graph.append(list(map(str,sys.stdin.readline().rstrip())))
  
def solution(x,y,N):
  check = int(graph[x][y])
  for i in range(x,x+N):
    for j in range(y,y+N):
      if int(graph[i][j])!=check:
        print("(",end="")
        solution(x,y,N//2)
        solution(x,y+N//2,N//2)
        solution(x+N//2,y,N//2)
        solution(x+N//2,y+N//2,N//2)
        print(")",end="")
        return
        
  if check==0:
    print(0,end="")
    
  else:
    print(1,end="")

start = graph[0][0]    
a = 2

for i in range(N):
  for j in range(N):
    if start==graph[i][j]:
      if i==(N-1) and j==(N-1):
        print(start)
        a = start
      else:
        pass
    else:
      break

if a==2:
  solution(0,0,N)
