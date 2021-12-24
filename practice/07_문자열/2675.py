T = int(input())

for _ in range(T):  
  a,b = map(str, input().split())
  a = int(a)
  data = list(b)
  for i in data:
    for _ in range(a):
      print(i,end="")
  print()