import sys

N = str(sys.stdin.readline())

x = list(N)
y = sorted(x,reverse=True)
for i in range(len(y)):
  print(y[i],end="")