N = int(input())

data = []

data.append(666)

i=1000

while len(data)<=10000:
  if '666' in str(i):
    data.append(i)
  i += 1
  
print(data[N-1])
