from datetime import datetime
import math

def solution(fees, records):
    answer = []
    
    dic = {}
    
    for i in records:
        a = i.split(' ')
        if a[1] not in dic:
            dic[a[1]] = [datetime.strptime(a[0],'%H:%M')]
        else:
            dic[a[1]].append(datetime.strptime(a[0],'%H:%M'))
    
    for i in sorted(dic.items()):
        fee = fees[1]
        
        if len(i[1]) % 2 != 0:
            i[1].append(datetime.strptime("23:59",'%H:%M'))
        
        flag = 0
        minute = 0
        while flag != len(i[1]):
            minute += (((i[1][flag+1]-i[1][flag]).seconds)/60)
            flag += 2
        
        if minute > fees[0]:
            fee += (math.ceil((minute - fees[0])/fees[2]) * fees[3])
        
        answer.append(fee)
            
            
    return answer