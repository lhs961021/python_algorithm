import sys

N = int(sys.stdin.readline())

count = 1
stk = []
result = []
z = 1

for _ in range(N):
  num = int(sys.stdin.readline())

  while count<=num:
    stk.append(count)
    result.append('+')
    count+=1

  if stk[-1]==num:
    stk.pop()
    result.append('-')
  else:
    z = 0

if z==0:
  print("NO")
else:
  for i in result:
    print(i)

# 구글링 했음 다시 풀어봐야함

  
  
  