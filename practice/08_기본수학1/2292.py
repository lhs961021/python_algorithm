x = int(input())

for i in range(1,33000):
  a = (3*i*i) - (3*i) + 1
  b = (3*i*i) + (3*i) + 1
  if (x>a) and (x<=b):
    print(i+1)
    break
  elif x==1:
    print(1)
    break
