from collections import Counter

def solution(topping):
    answer = 0
    
    if len(topping)==1:
        return 0
    
    brother = Counter(topping)
    king = set()
    
    for i in topping:
        if i in brother:
            brother[i]-=1
        
        if brother[i] == 0:
            del brother[i]
        
        king.add(i)
        if len(brother)==len(king):
            answer += 1
    
    return answer