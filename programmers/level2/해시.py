import heapq

def solution(phone_book):
    
    if len(phone_book)==1:
        answer = True
    else:
        heapq.heapify(phone_book)
        a = heapq.heappop(phone_book)
        z = len(a)
        answer = True
        
        while phone_book:
            b = heapq.heappop(phone_book)
            if a==b[:z]:
                answer = False
                break
            else:
                a = b
                z = len(a)
    
    
    return answer