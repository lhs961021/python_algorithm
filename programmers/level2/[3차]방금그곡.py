from datetime import datetime
import re

def solution(m, musicinfos):
    answer = ''
    
    def change(m):
        if 'C#' in m:
            m = m.replace('C#','H')
        if 'D#' in m:
            m = m.replace('D#','I')
        if 'F#' in m:
            m = m.replace('F#','J')
        if 'G#' in m:
            m = m.replace('G#','K')
        if 'A#' in m:
            m = m.replace('A#','L')
            
        return m

    m = change(m)
    p = []
    
    count = 0
    
    for i in musicinfos:
        s_time,e_time,name,melody = i.split(',')
        
        time = datetime.strptime(e_time,"%H:%M") - datetime.strptime(s_time,"%H:%M")
        minute = int((time.seconds)/60)
        melody = change(melody)
        j = melody*(minute//len(melody))+melody[:minute%len(melody)]

        if m in j:
            p.append((name,minute,count))
            count += 1
    
    if p:
        p.sort(key = lambda x : (-x[1],x[2]))
        return p[0][0]
    else:
        return "(None)"
