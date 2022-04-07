def solution(s):
    answer = -1
    
    a = []
    
    for i in s:
        if len(a)==0:
            a.append(i)
        elif a[len(a)-1]==i:
            a.pop()
        else:
            a.append(i)
    
    if len(a)==0:
        answer = 1
    else:
        answer = 0
    
    return answer