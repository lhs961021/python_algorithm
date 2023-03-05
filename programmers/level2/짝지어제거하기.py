from collections import deque

def solution(s):
    answer = 1
    
    queue = deque(s[0])
    
    for i in range(1,len(s)):
        if queue and queue[len(queue)-1]==s[i]:
            queue.pop()
        else:
            queue.append(s[i])
    
    if queue:
        return 0
    else:
        return 1
