N = int(input())


for j in range(1,N+1):
  for i in range(2,N+1):
    a = N/i
    if a==int(a):
      print(i)
      N = int(a)
      break
    else:
      pass
  
  if N==1:
    break
