def solution(n):
    answer = n
    
    a = bin(n)[2:].count('1')

    while 1:
        answer += 1
        if a == bin(answer)[2:].count('1'):
            break
            
    
    return answer