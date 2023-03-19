def solution(n, t, m, p):
    answer = ''
    
    dic = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    
    result = '0'
    for i in range(1,t*m):
        flag = ''
        while i > 0:
            i, mod = divmod(i, n)
            if mod in dic:
                flag += dic[mod]
            else:
                flag += str(mod)
        result += flag[::-1]
    
    check = 1    
    count = p
    
    while 1:
        for i in result:
            if check==count:
                answer += i
                if len(answer)==t:
                    return answer
                count += m 
            check += 1
            
    
    return answer