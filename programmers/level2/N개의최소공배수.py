from math import gcd

def solution(arr):
    
    def lcm(x, y):
        return x * y // gcd(x,y)
    
    answer = arr.pop()
    
    if not arr:
        return answer
    
    while arr:
        b = arr.pop()
        answer = lcm(answer,b)
    
    return answer