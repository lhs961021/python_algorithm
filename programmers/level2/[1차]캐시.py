from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    queue = deque()
    
    if cacheSize==0:
        return 5*len(cities)
    
    for i in cities:
        a = i.lower()
        if len(queue)==cacheSize:
            if a in queue:
                queue.remove(a)
                queue.append(a)
                answer += 1
            else:
                queue.popleft()
                queue.append(a)
                answer += 5
        else:
            if a in queue:
                queue.remove(a)
                queue.append(a)
                answer += 1
            else: 
                queue.append(a) 
                answer += 5
        
    return answer