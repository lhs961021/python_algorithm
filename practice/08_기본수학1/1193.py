x = int(input())

for i in range (1,x+1):
  a = (i*(i+1))/2
  b = ((i+1)*(i+2))/2
  if x==1:
    print("1/1")
    break
  elif (a<x) and (x<=b):
    z= i+1
    c = int(x-a)
    d = int(b-x+1)
    if (z%2==0):
      print(f'{c}/{d}')
      break
    else:
      print(f'{d}/{c}')
      break

