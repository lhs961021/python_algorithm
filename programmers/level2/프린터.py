from collections import deque, Counter

def solution(priorities, location):
    
    answer = 0
    
    queue = deque()
    
    c = Counter(priorities)
    
    
    check = list(set(priorities))
    check.sort(reverse=True)
    
    for idx,i in enumerate(priorities):
        queue.append((i,idx))
        
    flag = 0
    count = 0
    count_check = 0 
    
    for i in check:
        length = len(queue)
        flag = 0
        count = 0
        count_check = 0
        while length!=flag and count_check != c[i]:
            a = queue.popleft()
            flag += 1
            
            if a[0]==i:
                answer += 1
                if a[1]==location:
                    print(a)
                    return answer
                else:
                    count_check += 1
                    pass
            else:
                queue.append(a)

    return answer