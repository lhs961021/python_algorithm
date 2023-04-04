import time
start = time.time()

n = 1
m = 500000
answer = 0

for i in range(n,m+1):
    if str(i) == str(i)[::-1]:
        answer += 1

print(answer)

print("time :", time.time() - start)
