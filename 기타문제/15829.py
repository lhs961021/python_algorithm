import sys

N = int(sys.stdin.readline())

graph = list(input())

answer = []

for i in range(N):
  answer.append([ord(graph[i])-96,31**(i)])


sum_1 = 0

for i in range(N):
  sum_1 += (answer[i][0]*answer[i][1])

print(sum_1 % 1234567891)