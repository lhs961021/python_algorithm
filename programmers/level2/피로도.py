from itertools import permutations
from copy import deepcopy

def solution(k, dungeons):
    answer = -1
    
    for i in list(permutations([i for i in range(len(dungeons))],len(dungeons))):
        c = deepcopy(k)
        flag = 0
        for j in i:
            if c<dungeons[j][0]:
                break
            else:
                c -= dungeons[j][1]
                flag += 1
        
        answer = max(answer,flag)
        
    return answer