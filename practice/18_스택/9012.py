import sys

N = int(input())
   
for _ in range(N):
  s = str(sys.stdin.readline())
  while "()" in s:
    s = s.replace("()","")

  z = list(s.rstrip())
  
  if len(z)==0:
    print("YES")
  else:
    print("NO")