import math

N,M = map(int,input().split())

a = math.gcd(N,M)

print(a)

b = int(N/a)*M
print(b)    
  
