import sys

T = int(sys.stdin.readline())

for _ in range(T):
  a = list(str(sys.stdin.readline().rstrip()))
  a.reverse()

  s=''.join(a)
  k = s.split(' ')
  k.reverse()
  print(' '.join(k))
