while True:
    
  m = list(map(int,input()))

  if m==[0]:
    break

  j = list(reversed(m))

  if m==j:
    print("yes")
  else:
    print("no")
