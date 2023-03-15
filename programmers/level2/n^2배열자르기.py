import math

def solution(n, left, right):
    answer = []
    
    a = left//n
    b = left%n
    d = right-left
    
    count = 0
    
    while count!=(d+1):
        answer.append(max(a+1,b+1))
        if (b+1)==n:
            b = 0
            a += 1
        else:
            b+=1
        count+=1
        
    return answer