import re
from collections import Counter

def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    
    for i in range(len(str1)-1):
        if (str1[i:i+2].isalpha())==True:
            s1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if (str2[j:j+2].isalpha())==True:
            s2.append(str2[j:j+2])
    

    Counter1 = Counter(s1)
    Counter2 = Counter(s2)
    
    inter = list((Counter1&Counter2).elements())
    
    union = list((Counter1|Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    
import re
from collections import Counter

def solution(str1, str2):    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
             str1_list.append(str1[i:i+2].lower())
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
             str2_list.append(str2[i:i+2].lower())
    
    a = (Counter(str1_list) & Counter(str2_list)).values()
    result_1 = 0
    for i in a:
        result_1 += i
    
    
    b = (Counter(str1_list)|Counter(str2_list)).values()
    result_2 = 0
    for i in b:
        result_2 += i
    
    try:
        c = result_1/result_2
    except:
        c = 1
    answer = int(c*65536)
    
    return answer