import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())



def bfs():
  queue = deque([N])

  while queue:

    v = queue.popleft()

    if v==K:
      print(time[v])
      return

    for i in (v-1,v+1,v*2):
      if 0<= i <100001 and not time[i]:
        time[i] = time[v] + 1
        queue.append(i)

time = [0]*100001

bfs()
