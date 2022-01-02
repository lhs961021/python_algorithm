import sys

N,M = map(int, sys.stdin.readline().split())

z = []

data = [[0]*M for i in range(N)]

for i in range(N):
  l = sys.stdin.readline()
  k = 0
  for j in range(1,M+1):
    data[i][j-1] = l[k:j]
    k+=1

answer1 = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
answer2 = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]

p = []

for i in range(0,N-7):
  for j in range(0,M-7):
    count = 0
    z = 0
    for k in range(i,i+8):
      l = 0
      for m in range(j, j+8):
        if data[k][m] == answer1[z][l]:
          pass
        else:
          count+=1
        l+=1
      z +=1
    p.append(count)

for i in range(0,N-7):
  for j in range(0,M-7):
    count = 0
    z = 0
    for k in range(i,i+8):
      l = 0
      for m in range(j, j+8):
        if data[k][m] != answer2[z][l]:
          count+=1
        l+= 1
      z += 1
    p.append(count)

an = min(p)
print(an)

