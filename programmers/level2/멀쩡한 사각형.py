import math

def solution(w,h):
    answer = w*h - (w+h-math.gcd(w,h))
    return answer

def solution(w,h):
    answer = 0
    if w ==1 or h ==1:
        return 0
    
    if w == h:
        return sum(range(1,w))*2
    
    for i in range(1,w):
        answer += int((-(h/w)*i)+h)
        
    return answer*2