def solution(s):
    answer = ''
    a = s.split(' ')
    for i in a:
        if i == '':
            answer += ' '
        else:
            if i[0].isalpha():
                i = i[0].upper() + i[1:].lower()
                answer += i
                answer += ' '
            else:
                i = i[0] + i[1:].lower()
                answer += i
                answer += ' '
    
    answer = answer[:-1]
    
    return answer