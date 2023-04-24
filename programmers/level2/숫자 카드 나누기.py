# 카드 절반씩 나눠서 / 가장 큰 양의 정수 a
# 1. 철수 -> 최소공배수 영희 ->서로소
# 2. 영희 -> 최소공배수 철수 ->서로소
from itertools import combinations
from math import gcd

def solution(arrayA, arrayB):
    
    if len(arrayA)==1:
        if arrayA[0]==1 and arrayB[0]==1:
            return 0
        return max(arrayA[0],arrayB[0])
    
    
    array = arrayA+arrayB
    
    graph = []
    
    length = len(arrayA)

    def good(arrayA,arrayB):
        g = 0
        
        for i in arrayA:
            g = gcd(g,i)
        
        if g==1:
            return 1
        
        for j in arrayB:
            if j%g==0:
                return 0

        return g
        
    graph.append(good(arrayA,arrayB))
    graph.append(good(arrayB,arrayA))
    
    if max(graph[0],graph[1])==1:
        return 0
    else:
        return max(graph[0],graph[1])

