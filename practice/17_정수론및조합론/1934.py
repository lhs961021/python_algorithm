import math

n = int(input())

for _ in range(n):

  N,M = map(int,input().split())

  a = math.gcd(N,M)

  b = int(N/a)*M
  print(b)      
    