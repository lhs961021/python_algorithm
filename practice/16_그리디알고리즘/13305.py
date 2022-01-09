import sys

N = int(sys.stdin.readline())

distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

liter = sum(distance)

x = max(price)
y = price.index(x)

answer = 0

z = 0

for i in range(N-1):
  if price[i]==x and i==0:
    answer += (distance[i]*price[i])

  elif price[i]==x:
    answer += (price[z]*distance[i])

  else:
    if price[z]>price[i]:
      answer += (price[i]*distance[i])
      z = i

    else:
      answer += (price[z]*distance[i])

print(answer)