import math

def solution(k, d):
    answer = 0
    
    for a in range(0,d+1,k):
        b = (d**2-a**2)**0.5
        
        answer += math.ceil(b/k)
    
        if b%k == 0:
            answer += 1
        
        
    return answer