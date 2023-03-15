import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    queue = deque()
    
    for i,j in zip(progresses,speeds):
        queue.append(math.ceil((100-i)/j))
        
    while queue:
        a = queue.popleft()
        count = 1
        flag = 0
        for i in range(len(queue)):
            if a>=queue[i]:
                flag += 1
                count += 1
            else:
                answer.append(count)
                break
                
            if i==(len(queue)-1):
                answer.append(count)
                break
                
        for _ in range(flag):
            queue.popleft()
            
        if len(queue)==1:
            answer.append(1)
            break
            
    return answer