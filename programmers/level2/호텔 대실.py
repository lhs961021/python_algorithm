from datetime import datetime

def solution(book_time):
    answer = 0
    
    timeline = [0]*((24*60)+10)
    
    for i in book_time:
        a = i[0].replace(':','')
        b = i[1].replace(':','')
        
        a = int(a[:2])*60 + int(a[-2:])
        b = int(b[:2])*60 + int(b[-2:]) + 10
        
        for i in range(a,b):
            timeline[i]+=1
        
    
    return max(timeline)