import sys
 
N = int(input())

A = list(map(int,sys.stdin.readline().split()))

try:
  sum = 0

  for i in A:
    if (i!=1)and(i!=2):
      for j in range(2,i):
        m = i / j 
        if m==int(m):
          break
        else:
          if j==(i-1):
            sum +=1
    elif(i==2):
      sum+=1
    else:
      pass

  print(sum)

except:
  print(0)
  