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

def solution(numbers, target):
    answer = 0
    
    def dfs(count,idx,numbers):
        
        if idx==len(numbers):
            if count == target:
                return 1
            else:
                return 0
            
        return dfs(count-numbers[idx],idx+1,numbers) + dfs(count+numbers[idx],idx+1,numbers)
        
    answer = dfs(0,0,numbers)
    
    
    return answer