import sys
from collections import Counter

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

x = 0
y = 0

answer = []
start = graph[0][0]

def dfs(x,y,count):
  if x<0 or y<0 or x>N-1 or y>N-1:
    return False
  if graph[x][y]==1:
    answer.append(count)  
    graph[x][y]+=1
    dfs(x-1,y,count)
    dfs(x,y-1,count)
    dfs(x+1,y,count)
    dfs(x,y+1,count)
    return True
  return False

result = 0
count = 0

for i in range(N):
  for j in range(N):
    if dfs(i,j,count)==True:
      result +=1
      count+=1

answer_1= Counter(answer)
answer_1 = sorted(answer_1.values())

print(result)
for i in range(len(answer_1)):
  print(answer_1[i])