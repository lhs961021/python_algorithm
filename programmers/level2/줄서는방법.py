from itertools import permutations
from math import factorial

def solution(n, k):
    
    answer = []
    l = [i for i in range(1,n+1)]

    k -= 1
    while n != 0:
        num,k = divmod(k,factorial(n-1))
        answer.append(l.pop(num))
        n-=1
        
    return answer

