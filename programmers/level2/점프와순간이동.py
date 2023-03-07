def solution(n):
    ans = 1
    flag = 0
    
    while n!=1:
        if n%2!=0:
            ans += 1
        
        n = n//2
        
        
    return ans