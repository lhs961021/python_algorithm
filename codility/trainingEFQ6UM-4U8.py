# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binaryNum = bin(N)

    print(binaryNum)

    flag = 0
    answer = 0
    count = 0

    for i in binaryNum[2:]:
        if i=='1':
          if flag==0:
            count = 0
          else:
            if answer<count:
              answer = count
            flag = 0
            count = 0    
        else:
            count += 1
            flag = 1

    return answer
