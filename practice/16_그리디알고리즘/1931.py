import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
  a,b = map(int,sys.stdin.readline().split())
  data.append([a,b])

data.sort(key = lambda data : data[0])
data.sort(key = lambda data : data[1])

count = 0
last = 0

for i,j in data:
  if i>=last:
    count += 1
    last = j

print(count)


# 구글링했음 / 생각조차 못한문제 꼭 풀어보기
# sort에 조건을 걸수 있다 => key를 통해 건다 처음알았음
# 2차원 배열일때 for 문에서 두가지 인자를 부르면 두개 인자 만 나옴
