from collections import deque

def solution(numbers, target):
    queue = deque()
    answer = 0
    queue.append((numbers[0],0))
    queue.append((-numbers[0],0))

    while queue:
        temp, cnt = queue.popleft()

        cnt += 1

        if cnt<len(numbers):
            queue.append((temp+numbers[cnt],cnt))
            queue.append((temp-numbers[cnt],cnt))

        else:
            if temp==target:
                answer += 1

    return answer