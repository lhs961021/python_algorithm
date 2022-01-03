import sys

N = int(input())

data = [0]*10001

for _ in range(N):
  i = int(sys.stdin.readline())
  data[i-1] = data[i-1]+1

for i in range(10001): 
  if data[i] != 0:
    for j in range(data[i]):
      print(i+1) 
      

