# import sys

# N = int(sys.stdin.readline())

# data = list(sys.stdin.readline().split())

# answer = []

# for i in range(N):
#   count = 0
#   k = []
#   for j in range(N):
#     if i!=j:
#       if data[j] in k:
#         pass
#       else:
#         if int(data[i])>int(data[j]):
#           count+=1
#           k.append(data[j])
#   answer.append(count)  

# for i in range(N):
#   print(answer[i],end=" ")

#내가 짠 코드

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ') 

# 구글링
# dictionary 이용
