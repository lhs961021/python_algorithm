import sys
from collections import deque

n = int(sys.stdin.readline())

def cal_D(n):
  res = n * 2
  if res > 9999:
    res = res % 10000
  return res

def cal_S(n):
  res = n
  if res == 0:
    return 9999
  res = n - 1
  return res

def cal_L(n):
  first = n % 1000
  last = n // 1000 
  res =  first * 10 + last
  return res 

def cal_R(n):
  first = n % 10
  last = n//10
  res = first * 1000 + last
  return res  

def func(a,b):
  queue = deque()
  visited = set()
  queue.append((a,""))
  visited.add(a)
  while queue:
    num, answer = queue.popleft()
    if num == b:
      print(answer)

    tmp = cal_D(num)
    if tmp not in visited:
      visited.add(tmp)
      queue.append((tmp,answer+"D"))
      
    tmp = cal_S(num)
    if tmp not in visited:
      visited.add(tmp)
      queue.append((tmp,answer+"S"))
      
    tmp = cal_L(num)
    if tmp not in visited:
      visited.add(tmp)
      queue.append((tmp,answer+"L"))
      
    tmp = cal_R(num)
    if tmp not in visited:
      visited.add(tmp)
      queue.append((tmp,answer+"R"))

for _ in range(n):
  a,b = map(int,sys.stdin.readline().split())

  func(a,b)

  

      

                                                                                                         

    
 
  


  
 