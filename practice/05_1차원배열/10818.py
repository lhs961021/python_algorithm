import sys

N = int(input())

data = list(map(int,sys.stdin.readline().split()))

print(min(data),end=" ")
print(max(data),end=" ")