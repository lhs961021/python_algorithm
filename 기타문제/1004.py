import sys

T = int(sys.stdin.readline())

for _ in range(T):
  start_x,start_y,end_x,end_y = map(int,sys.stdin.readline().split())

  n = int(sys.stdin.readline())

  graph = []
  answer = 0

  for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

  for i in range(n):
    x = graph[i][0]
    y = graph[i][1]
    r = graph[i][2]

    flag = 1

    if((abs(start_x-x)**2)+(abs(start_y-y)**2))<=(r*r):
      answer += 1
      flag = 0

    if((abs(end_x-x)**2)+(abs(end_y-y)**2))<=(r*r):
      if flag==0:
        answer -= 1
      else:
        answer += 1

  print(answer)

