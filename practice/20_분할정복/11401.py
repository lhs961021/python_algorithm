import sys

MOD = 1000000007

N,K = map(int,sys.stdin.readline().split())

def factorial(n):
  if n==0:
    return 1
  
  for i in range(n-1,1,-1):
    n = (n*i)%MOD
  return n

def fast_pow(x,n):
  if n==0:
    return 1
  elif n==1:
    return x%MOD
  elif n%2==0:
    return (fast_pow(x,n//2)**2) % MOD
  else:
    return (fast_pow(x,n//2)**2*x) % MOD  


a = factorial(N)
b = fast_pow(factorial(K), MOD-2)%MOD
c = fast_pow(factorial(N-K), MOD-2)%MOD

print(a*b*c%MOD)