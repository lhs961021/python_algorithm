import sys

A,B,C = map(int,sys.stdin.readline().split())

def solution(a,n):
  if n==1:
    return A%C
  else:
    tmp = solution(a,n//2)
    if n%2==0:
      return (tmp*tmp)%C
    else:
      return (tmp*tmp*A)%C

print(solution(A,B))  

# 수학 분배법칙 숙지 필요(구글링)