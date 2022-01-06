from math import factorial

N = int(input())
for _ in range(N):  
  k, n = map(int, input().split())
  result = factorial(n) // (factorial(k) * factorial(n - k))
  print(result)