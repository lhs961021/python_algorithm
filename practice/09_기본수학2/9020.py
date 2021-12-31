import sys

def isPrime(num):
  if num==1:
    return False
  else:
    for i in range(2, int(num**0.5)+1):
      if num%i==0:
        return False
    return True

data = list(range(2,10001))
data_1 = []
for i in data:
  if isPrime(i):
    data_1.append(i)

N = int(sys.stdin.readline())

for _ in range(N):
  A = int(sys.stdin.readline())

  for i in range(A//2,1,-1):
    if i in data_1:
      j = A-i
      if j in data_1:
        print(i,end=" ")
        print(j)
        break


  
