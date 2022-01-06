import sys
import math

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

for i in range(1,N):
  a = math.gcd(data[0],data[i])
  b = int(data[0]/a)
  c = int(data[i]/a)
  print(f'{b}/{c}')