import sys

a = int(input())

d = list(set(map(int,sys.stdin.readline().split())))

print(*sorted(d))