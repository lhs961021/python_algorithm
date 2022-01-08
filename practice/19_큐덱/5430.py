import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
  data = sys.stdin.readline().rstrip()
  n = int(sys.stdin.readline())
  z = sys.stdin.readline().rstrip()[1:-1].split(",")

  if z[0] != '':
    z = deque(z)
  else:
    z = deque()

  rev = 0
  flag = 0
   
  for i in data:
    if i=='R':
      rev += 1
    else:
      if len(z)<1:
        flag = 1
        print("error")
        break
      else:  
        if rev % 2 == 0:
          z.popleft()
        else:
          z.pop()

  if flag==0:
    if data.count('R') % 2 != 0 :
      z.reverse()
      print("[" + ",".join(z) + "]")
    else:
      print("[" + ",".join(z) + "]")
      
# 예외처리부분 구글링 -> 왜 try,except 구문 안되는지 모르겠음 출력은 맞는데,,

  
  

  

