def solution(name):
    answer = 0
    alphabet = ['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T',
               'U','V','W','X','Y','Z']
    
    length = len(name)
    
    if len(name)==1:
        return alphabet.index(name[0])

    min_move = length-1
    
    for idx,i in enumerate(name):
        k = alphabet.index(i)
        answer += min((26-k),k)
        
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 2 *idx + len(name) - next, idx + 2 * (len(name) -next)])  
    
    answer += min_move
      
            
    return answer
