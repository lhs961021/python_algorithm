import re

def solution(p):
    answer = ''
    def check(u):
        while u.count('()'):
            u = re.sub('\(\)','',u)

        return u
    
    def reverse(u):
        u = u[1:-1]
        a = ''
        
        for i in u:
            if i == '(':
                a += ')'
            else:
                a += '('
        
        return a
    
    def find(w):
        if w == '':
            return ''
        
        l_count = 0
        r_count = 0
        
        for i in range(len(w)):
            if w[i] == '(':
                l_count += 1
            else:
                r_count += 1

            if l_count==r_count:
                u = w[:i+1]
                v = w[i+1:]
                
                if check(u) != '':
                    return '('+find(v)+')'+reverse(u)
                else:
                    return u + find(v)
            
    answer += find(p)
        
    return answer