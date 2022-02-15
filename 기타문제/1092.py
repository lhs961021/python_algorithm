import sys
from collections import deque

N = int(sys.stdin.readline())

crane = list(map(int,sys.stdin.readline().split()))

crane.sort(reverse=True)

M = int(sys.stdin.readline())

box = list(map(int,sys.stdin.readline().split()))

box.sort(reverse=True)

answer = 0

if box[0]>crane[0]:
  print(-1)
  
else:
  while box:
  
    z = deque(crane)
  
    while z:
      a = z.popleft()
  
      for i in range(len(box)):
        if box[i]<=a:
          box.remove(box[i])
          break
         
    answer += 1

  print(answer)
        
        
  
