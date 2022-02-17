import sys

string = str(sys.stdin.readline().rstrip())
bomb = str(sys.stdin.readline().rstrip())
l = len(bomb)
b = bomb[-1]
stk = []

for s in string:
  stk.append(s)
  if s==b and ''.join(stk[-l:])==bomb:
    for _ in range(l):
      stk.pop()

if stk:
  print(f"{''.join(stk)}")
else:
  print("FRULA")
  