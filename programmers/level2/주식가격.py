from collections import deque

def solution(prices):
    answer = []
    
    queue = []
    prices = deque(prices)
    
    while prices:
        a = prices.popleft()
        flag = 0
        
        for i in prices:
            flag += 1
            if a>i:
                break

        answer.append(flag)
        
    return answer