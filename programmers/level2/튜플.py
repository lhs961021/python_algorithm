def solution(s):
    answer = []

    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
                
    
    return answer

def solution(s):
    answer = []
    
    s = s.replace('{','').replace(',',' ').replace('}','')
    
    dic = {}
    
    for i in s.split(' '):
        if i.isdigit():
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

    for i in sorted(dic.items(), key = lambda x : -x[1]):
        answer.append(int(i[0]))
    
    
    return answer