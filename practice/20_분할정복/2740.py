import sys

A = []
B = []

N,M = map(int,sys.stdin.readline().split())

for _ in range(N):
  A.append(list(map(int,sys.stdin.readline().split())))

M,K = map(int,sys.stdin.readline().split())

for _ in range(M):
  B.append(list(map(int,sys.stdin.readline().split())))

def solution(x,y):
  answer = 0
  for i in range(M):
    answer += (A[x][i]*B[i][y])
  return answer


for i in range(N):
  for j in range(K):
    print(solution(i,j),end=" ")
  print()



