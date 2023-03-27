from collections import deque

def solution(n, m, section):
    answer = 0
    
    if m == 1:
        return len(section)
    
    queue = deque(section)
    
    while queue:
        v = queue.popleft()
        flag = 0
        
        for i in queue:
            if v<=i<=v+m-1:
                flag += 1
            else:
                break
        
        answer += 1
        
        for _ in range(flag):
            queue.popleft()
        
        
    
    return answer