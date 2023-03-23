def solution(numbers):
    
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    
    return answer

def solution(numbers):

    answer = ''
    
    numbers = list(map(str, numbers))

    numbers.sort(reverse = True, key = lambda x: (x*4)[:4])
    
    answer = ''.join(numbers)
    
    if answer[0]=='0':
        return '0'
    
    return answer