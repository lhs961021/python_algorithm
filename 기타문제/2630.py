import sys

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

white = 0
blue = 0

def solution(x,y,n):
  global blue,white
  check = graph[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if check!=graph[i][j]:
        solution(x,y,n//2)
        solution(x,y+n//2,n//2)
        solution(x+n//2,y,n//2)
        solution(x+n//2,y+n//2,n//2)
        return

  if check==0:
    white +=1
  else:
    blue += 1
    return

solution(0,0,n)
print(white)
print(blue)

# 구글링 했음. 분할정복 처음 