def solution(s):
    answer = 10000
    a = len(s)
    
    if len(s)==1:
        return 1
    
    for i in range(1,a//2+1):
        cnt = 1
        tmp = s[:i]
        res = ''
        
        
        for j in range(i,len(s),i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                tmp = s[j:i+j]
                cnt = 1
        
        if cnt!=1:
            res+=str(cnt)+tmp
        else:
            res+=tmp
        
        
        answer = min(answer,len(res))

    return answer