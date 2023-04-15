import heapq

def solution(operations):
    answer = []
    
    queue_l = []
    queue_r = []
    
    for i in operations:
        do,num = i.split(' ')
        
        if do == 'I':
            heapq.heappush(queue_l,int(num))
            heapq.heappush(queue_r,-int(num))
        else:
            if queue_l or queue_r:
                if num == '-1':
                    a = heapq.heappop(queue_l)
                    queue_r.remove(-a)
                else:
                    a = heapq.heappop(queue_r)
                    queue_l.remove(-a)
                                
    if queue_l==[]:
        return [0,0]
        
    
    return [max(queue_l),min(queue_l)]