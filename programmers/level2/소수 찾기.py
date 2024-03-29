from itertools import permutations
import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x==1 or x==0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(numbers):
    answer = 0
    graph = []
    for i in range(1,len(list(numbers))+1):
        for j in permutations(list(numbers), i):
            st = ''
            for z in list(j):
                st += z 
            graph.append(int(st))
            
    k = list(set(graph))
    
    for i in k:    
        if is_prime_number(int(i))==True:
            answer += 1
    
    return answer

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    l = set()
    
    def check(num):
        if num==1:
            return False
        
        if num==2:
            return True
        
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        
        return True
    
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            num = ''.join(j)
            if j[0]!='0' and num not in l:
                l.add(num)
                if check(int(num))==True:
                    answer += 1
    
    return answer