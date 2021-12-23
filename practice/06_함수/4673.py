data = []
def d(n):
  if n<100: 
    n = (n%10)+(n//10)+n
  elif n<1000:
    n = (n//100)+(n//10%10)+(n%100%10)+n
  elif n<10000:
    n = (n//1000)+(n//100%10)+(n%100//10)+(n%1000%100%10)+n
  data.append(n)

for i in range(1,10001):
  d(i)

for i in range(1,10001):
  if i not in data:
    print(i)
