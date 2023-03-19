def solution(msg):
    answer = []
    
    dic = {}
    flag = 65
    
    for i in range(1,27):
        dic[chr(flag)] = i
        flag += 1

    check = msg[0]
    for i in range(1,len(msg)):
        check += msg[i] 
        if check not in dic:
            dic[check] = len(dic)+1
            answer.append(dic[check[:-1]])
            check = msg[i]
    
    answer.append(dic[check])
        
    return answer