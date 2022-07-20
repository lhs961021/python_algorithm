import sys

N,r,c = map(int,sys.stdin.readline().split())

count = 0

while N!=0:
  N -= 1
  end = 2**N
  
  if r>=end and c>=end:
    count += (end*end)*3
    c -= end
    r -= end
  elif r>=end and c<end:
    count += (end*end)*2
    r -= end
  elif r<end and c>=end:
    count += (end*end)
    c -= end

print(count)