from itertools import permutations
import re
from copy import deepcopy
from collections import deque

def solution(expression):
    answer = 0
    
    number = list(re.split('([-\+\*])',expression))
    
    cal = list(permutations(['-','+','*'],3))
    
    for i in cal:
        result = 0
        num = deepcopy(number)
        while num.count(i[0]):
            for j in range(len(num)):
                if num[j] == i[0]:
                    a = eval(num[j-1] + num[j] + num[j+1])
                    result += a
                    num = num[:j-1] + [str(a)] + num[j+2:]
                    break
        
        while num.count(i[1]):
            for j in range(len(num)):
                if num[j] == i[1]:
                    a = eval(num[j-1] + num[j] + num[j+1])
                    result += a
                    num = num[:j-1] + [str(a)] + num[j+2:]
                    break
        
        while num.count(i[2]):
            for j in range(len(num)):
                if num[j] == i[2]:
                    a = eval(num[j-1] + num[j] + num[j+1])
                    result += a
                    num = num[:j-1] + [str(a)] + num[j+2:]
                    break
        
        answer = max(abs(int(num[0])),answer)

        
    return answer