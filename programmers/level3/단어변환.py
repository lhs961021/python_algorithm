from collections import deque

def solution(begin, target, words):
    
    answer = 123412341234
    
    if target not in words:
        return 0
    
    length = len(words)
    
    queue = deque()
    
    visited = [0]*length
    
    def check(word1,word2):
        count = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                count += 1
        
        if count == 1:
            return True
        else:
            return False
    
    for i in range(length):
        if check(begin,words[i])==True:
            queue.append((i,1))
    
    while queue:
        a,cnt = queue.popleft()
        visited[a] = 1
        
        if words[a]==target:
            answer = min(answer,cnt)
                
        for i in range(length):
            if visited[i] != 1:
                if check(words[a],words[i])==True:
                    queue.append((i,cnt+1))
    
    return answer
    