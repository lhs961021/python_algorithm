from collections import deque

def solution(order):
    answer = 0
    
    truck = deque([i for i in range(1,len(order)+1)])

    queue = deque() # 보조
    
    flag = 0
    
    while 1:
        if truck:
            if order[flag] == truck[0]:
                flag += 1
                truck.popleft()
                answer += 1
                continue
        
        if queue:
            if order[flag] == queue[-1]:
                flag += 1
                queue.pop()
                answer += 1
                continue
        
        if truck:
                a = truck.popleft()
                queue.append(a)
        else:
            break
                
        if len(order)==0 and len(queue)==0:
            break
    
    return answer

