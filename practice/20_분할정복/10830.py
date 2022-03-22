import sys

N,B = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

def solution(a,b):
  
  product = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      for k in range(N):
        product[i][j] += a[i][k] * b[k][j]
      product[i][j]%=1000
     
  return product
  
def divide(N,B):
  if B==1:
    return graph
  elif B==2:
    return solution(graph,graph)
  else:
    tmp = divide(N,B//2)
    
    if B%2==0:
      return solution(tmp,tmp)
    else:
      return solution(solution(tmp,tmp),graph)

result = divide(N,B)
for i in result:
  for j in i:
    print(j%1000,end=" ")
  print()