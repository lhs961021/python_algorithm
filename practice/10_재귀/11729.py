def hanoi(num,x,y):
    if num>1:
        hanoi(num-1,x,6-x-y)
  
    data.append([x,y])
  
    if num>1:
        hanoi(num-1,6-x-y,y)
  
N = int(input())
data = []
hanoi(N,1,3)

print(len(data))
for i in range (len(data)):
  print(data[i][0],end=" ")
  print(data[i][1])

