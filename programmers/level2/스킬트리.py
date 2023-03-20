def solution(skill, skill_trees):
    answer = 0
    
    arr = []
    
    for j in range(1,len(skill)):
        arr.append(skill[0:j])
        
    arr.append(skill)
    
    for i in skill_trees:
        queue = ''
        
        for j in i:
            if j in skill:
                queue+=j
        
        if queue=="":
            answer += 1
        else:
            if queue in arr:
                answer += 1
            
    return answer