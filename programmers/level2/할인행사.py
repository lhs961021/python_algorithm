from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    dic = {}
    for i,j in zip(want,number):
        dic[i] = j
    
    if len(discount)==10:
        if (Counter(discount).items() == dic.items()):
            return 1
        else:
            return 0
    
    for i in range(len(discount)-9):
        if (Counter(discount[i:i+10]).items()==dic.items()):
            answer += 1
            
    return answer