def solution(id_list, report, k):
    answer = []
    
    dic = {}
    
    for i in id_list:
        dic[i] = [[],0]
    
    for j in report:
        a,b = j.split(' ')
        if b not in dic[a][0]:
            dic[a][0].append(b)
            dic[b][1] += 1
    
    for m in dic.items():
        flag = 0
        for l in m[1][0]:
            if dic[l][1]>=k:
                flag += 1
        answer.append(flag)
        
    return answer