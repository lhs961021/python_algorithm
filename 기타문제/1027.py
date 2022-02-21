import sys

graph = [0]*50

N = int(sys.stdin.readline())

building = list(map(int,sys.stdin.readline().split()))

for i in range(N):
  s = []
  p = []
  answer = 0
  flag = 0
  for j in range(i,-1,-1):
    if i!=j:
      a1 = float((building[i]-building[j])/((i+1)-(j+1)))
      if not s:
        s.append(a1)
        answer += 1
      else:
        if s[len(s)-1]>a1:
          s.append(a1)
          answer += 1
          
  for j in range(i,N):
    if i!=j:
      a1 = float((building[j]-building[i])/((j+1)-(i+1)))
      if not p:
        p.append(a1)
        answer +=1
      else:
        if p[len(p)-1]<a1:
            p.append(a1)
            answer += 1
            
  graph[i]=answer

print(max(graph))
    
      