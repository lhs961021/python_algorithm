def solution(n):
    answer = 1
    
    flag = 1

    while flag!=n:
        a = 0 
        for i in range(flag,n):
            a += i
            if a==n:
                answer += 1
                break
            elif a>n:
                break
            else:
                pass
        flag += 1
    
    return answer