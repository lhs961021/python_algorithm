data = []
def d(n):
  if n<100:
    data.append(n)
  elif n<1000:
    a = n//100
    b = n%100//10
    c = n%100%10
    if ((2*b)==(a+c)):
      data.append(n)
  else:
    return
  

N = int(input())

for i in range(1,N+1):
  d(i)

sum = 0

for i in range(1,N+1):
  if i in data:
    sum += 1

print(sum)
