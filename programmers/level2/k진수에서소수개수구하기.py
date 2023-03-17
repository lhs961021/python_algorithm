import math

def check(num):
    if num==1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    result = ''

    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    
    a = result[::-1] 

    p = a.split('0')
    
    for i in p:
        if i!='':
            if check(int(i))==True:
                answer += 1

    return answer