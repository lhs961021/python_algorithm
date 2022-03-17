import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

minus_1 = 0
zero = 0
plus_1 = 0
    
def solution(x,y,N):
  global minus_1
  global zero
  global plus_1  
  
  check = graph[x][y]
  for i in range(x,x+N):
    for j in range(y,y+N):
      if graph[i][j]!=check:
        for k in range(3):
          for l in range(3):
            solution(x+k*N//3,y+l*N//3,N//3)
        return
        
  if check==-1:
    minus_1 += 1
    
  elif check==0:
    zero += 1

  else:
    plus_1 += 1

solution(0,0,N)

print(minus_1)
print(zero)
print(plus_1)
