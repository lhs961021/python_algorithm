import sys

N = int(sys.stdin.readline())

answer = []

for _ in range(N):
  A = str(sys.stdin.readline())

  if 'add' in A:
    a,b = A.split()
    if int(b) not in answer:
      answer.append(int(b))
  elif 'remove' in A:
    a,b = A.split()
    if int(b) in answer:
      answer.remove(int(b))
  elif 'check'  in A:
    a,b = A.split()
    if int(b) in answer:
      print(1)
    else:
      print(0)
  elif 'toggle' in A:
    a,b = A.split()
    if int(b) in answer:
      answer.remove(int(b))
    else:
      answer.append(int(b))
  elif 'all' in A:
    answer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  else:
    answer = []



