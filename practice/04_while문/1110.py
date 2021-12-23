a = int(input())

i = a
n = 0

while True:
  if i<10:
    i = (10*i)+i
    n += 1
  else:
    b = i//10
    c = i-(b*10)
    d = b+c
    if d>=10:
      e = d%10
    else:
      e = d
    i = (c*10)+e
    n += 1

  if(i==a):
    break

print(n)