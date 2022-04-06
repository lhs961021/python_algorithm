import math

def solution(progresses, speeds):
    
    queue = []
    
    
    for i in range(len(progresses)):
        k = math.ceil((100-progresses[i])/speeds[i])
        queue.append(k)
    
    answer = []

    count = 1
    
    flag = queue[0]


    for i in range(1,len(queue)):
        if queue[i]-flag<=0:
            count += 1
        else:
            answer.append(count)
            count = 1
            flag = queue[i]

    answer.append(count)
    
    
    return answer