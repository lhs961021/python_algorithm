from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    ch_queue = deque(priorities)
    
    check = max(priorities)
    count = 0
    
    for i in range (len(priorities)):
        queue.append((priorities[i],i))
    
    while queue:
        p,num  = queue.popleft()
        z = ch_queue.popleft()
        
        if p==check:
            count += 1
            check = max(ch_queue)
            if num==location:
                answer = count
                break
            if len(queue)==1:
                answer = count+1
                break
            
        else:
            queue.append((p,num))
            ch_queue.append(z)

    return answer