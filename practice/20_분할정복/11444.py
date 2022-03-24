import sys

N = int(sys.stdin.readline())

graph = [[1,1],[1,0]]

def solution(a,b):
  
  product = [[0]*2 for _ in range(2)]

  for i in range(2):
    for j in range(2):
      for k in range(2):
        product[i][j] += a[i][k] * b[k][j]
      product[i][j]%=1000000007
     
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

result = divide(graph,N)

print(result[0][1]%1000000007)