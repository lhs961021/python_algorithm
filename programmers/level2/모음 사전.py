from itertools import product

def solution(word):
    answer = 0
    
    dic = []

    for i in range(1,6):
        dic.extend(list(product(['A','E','I','O','U'],repeat = i)))
    
    dic.sort()
    
    for idx,i in enumerate(dic):
        if word == ''.join(i):
            return idx+1
    
    return -1