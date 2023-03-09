def solution(clothes):
    answer = 1
    
    dic = {}
    
    for i in clothes:
        if i[1] in dic:
            dic[i[1]]+=1
        else:
            dic[i[1]] = 2
    
    for j in dic.values():
        answer *= j
    
    answer -= 1
        
    return answer