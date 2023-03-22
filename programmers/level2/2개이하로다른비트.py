def solution(numbers):
    answer = []
    
    for i in numbers:
        if i%2==0:
            answer.append(i+1)
        else:
            num = bin(i)[2:][::-1]
            try:
                a = 2**(num.index('0'))
                b = a//2
            except:
                a = 2**(len(num))
                b = a//2
            answer.append(i+a-b)
            
            
    return answer