import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while 1:
        small = heapq.heappop(scoville)
        
        if small>=K:
            break
        
        if len(scoville)==0:
            return -1
        
        least = heapq.heappop(scoville)
        
        new = small + (least*2)    
        heapq.heappush(scoville,new)
        answer += 1

    return answer