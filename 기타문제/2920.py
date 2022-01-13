import sys

a = [1,2,3,4,5,6,7,8]
b = [8,7,6,5,4,3,2,1]

m = list(map(int,sys.stdin.readline().split()))

if m==a:
  print("ascending")
elif m==b:
  print("descending")
else:
  print("mixed")