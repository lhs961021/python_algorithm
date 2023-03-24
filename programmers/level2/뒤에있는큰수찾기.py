def solution(numbers):
    answer = [-1]*len(numbers)
    
    stack = []
    
    for i in range(len(numbers)):
        value = numbers[i]
        while stack and numbers[stack[-1]] < value:
            answer[stack[-1]] = value
            stack.pop()
                
        stack.append(i)
                
    return answer