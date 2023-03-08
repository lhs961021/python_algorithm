import re

def solution(s):
    answer = 0
    checks = ['()','[]','{}']
    
    for i in range(len(s)):
        a = s[i:]+s[:i]
        while 1:
            a = re.sub('\[]|\(\)|{}',"",a)
            if a == "":
                answer += 1
                break
            
            if not any(check in a for check in checks):
                break
    
    return answer