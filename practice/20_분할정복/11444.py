import sys

N = int(sys.stdin.readline())

graph = [[1,1],[1,0]]

def solution(a,b): #a와 b는 그래프(행렬)
  
  product = [[0]*2 for _ in range(2)]

  for i in range(2): # 2X2 행렬
    for j in range(2): # 2X2 행렬
      for k in range(2): # 2X2 행렬
        product[i][j] += a[i][k] * b[k][j]
      product[i][j]%=1000000007
     
  return product #곱한 행렬을 반환
  
def divide(N,B): #이분탐색 N 그래프, B는 곱하는 수
  if B==1:
    return graph
  elif B==2:
    return solution(graph,graph)
  else:
    tmp = divide(N,B//2)
    
    if B%2==0:
      return solution(tmp,tmp) #짝수이면 한번 
    else:
      return solution(solution(tmp,tmp),graph) #홀수이면 짝수 꺼에 graph한번 더 곱하기

result = divide(graph,N)

print(result[0][1]%1000000007)