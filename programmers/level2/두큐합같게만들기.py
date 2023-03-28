from collections import deque

def solution(queue1, queue2):
    answer = 0
    result = (sum(queue1)+sum(queue2))/2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    count = (len(queue1)+len(queue2))*2
    
    s_q1 = sum(queue1)
    s_q2 = sum(queue2)
    
    while s_q1!=s_q2:
        if s_q1>s_q2:
            a = queue1.popleft()
            queue2.append(a)
            s_q1-=a
            s_q2+=a
        else:
            a = queue2.popleft()
            queue1.append(a)
            s_q2-=a
            s_q1+=a
            
        answer += 1
        count -= 1

        if count==0:
            return -1
        
    return answer