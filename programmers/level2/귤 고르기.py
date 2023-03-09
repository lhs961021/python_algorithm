from collections import Counter

def solution(k, tangerine):
    answer = 0
    flag = 0
    
    for i in sorted((Counter(tangerine)).items(), key = lambda x : -x[1]):
        answer += 1
        flag += i[1]
        
        if flag>=k:
            break
    
    return answer