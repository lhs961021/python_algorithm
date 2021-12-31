import sys

def isPrime(num):
  if num==1:
    return False
  else:
    for i in range(2, int(num**0.5)+1):
      if num%i==0:
        return False
    return True

data = list(range(2,246912))
data_1 = []
for i in data:
  if isPrime(i):
    data_1.append(i)

while(1):
  N = int(sys.stdin.readline())
  if N==0:
    break
  sum = 0
  for i in data_1:
    if N < i <= N*2:
      sum += 1
    
  print(sum)

    

# 제곱근을 이용해서 구한다.   